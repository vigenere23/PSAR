import cv2
import imutils
import numpy as np
import math

def nextOddNumber(number):
    return 2*math.floor(number/2)+1

def imageFromPercentile(image, percentile):
    newImage = image.copy()
    percentile = np.percentile(newImage[::-1], percentile)

    width = newImage.shape[0]
    height = newImage.shape[1]

    for w in range(width):
        for h in range(height):
            values = newImage[w][h]
            mean = values[0] + values[1] + values[2]
            mean/=3
            if(mean< percentile):
                newImage[w][h] = [0,0,0]

    return newImage

def maxValueInNeighborhood(results, position, range_delta_x=5, range_delta_y=5):
    maxValue = 0

    half_range_x = round(range_delta_x/2)
    half_range_y = round(range_delta_y/2)
    low_x_offset = -half_range_x
    high_x_offset = half_range_x
    low_y_offset = -half_range_y
    high_y_offset = half_range_y

    for h_offset in range(low_y_offset,high_y_offset+1):
        for w_offset in range(low_x_offset,high_x_offset+1):
            y_offset = h_offset + position[1]
            x_offset = w_offset + position[0]
            res_val = results[y_offset][x_offset]
            if(res_val>maxValue):
                maxValue =res_val

    return maxValue


def findPositionsInBoard(board_predictions):
    board_best = np.zeros((3,3), dtype=int)
    best_sum = 0

    for h in range(board_predictions.shape[1]-2):

        for w in range(board_predictions.shape[0]-2):

            current_sum = 0

            current_sum+=board_predictions[h][w][3]
            current_sum+=board_predictions[h][w+1][3]
            current_sum+=board_predictions[h][w+2][3]
            current_sum+=board_predictions[h+1][w][3]
            current_sum+=board_predictions[h+1][w+1][3]
            current_sum+=board_predictions[h+1][w+2][3]
            current_sum+=board_predictions[h+2][w][3]
            current_sum+=board_predictions[h+2][w+1][3]
            current_sum+=board_predictions[h+2][w+2][3]

            if(current_sum>best_sum):
                best_sum=current_sum
                current_board = np.zeros((3,3), dtype=int)
                current_board[0][0]= board_predictions[h][w][2]
                current_board[0][1]= board_predictions[h][w + 1][2]
                current_board[0][2]= board_predictions[h][w + 2][2]
                current_board[1][0]= board_predictions[h + 1][w][2]
                current_board[1][1]= board_predictions[h + 1][w + 1][2]
                current_board[1][2]= board_predictions[h + 1][w + 2][2]
                current_board[2][0]= board_predictions[h + 2][w][2]
                current_board[2][1]= board_predictions[h + 2][w + 1][2]
                current_board[2][2]= board_predictions[h + 2][w + 2][2]
                board_best = current_board

    return board_best


if __name__ == '__main__':

    pannel_path = "output.png"
    img_rgb = cv2.imread(pannel_path)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    (thresh, blackAndWhiteImage) = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

    template = cv2.imread('clockwise.png',0)
    template_counterclockwise = cv2.imread('counterclockwise.png',0)
    w, h = template.shape[::-1]
    w_c, h_c = template_counterclockwise.shape[::-1]

    highest_value = 0
    scale_highest_value = 1

    downsize_factor = 0.3
    upsize_factor = 2

    smallest_scale = 0.05
    biggest_scale = 0.6

    max_rotation = 0.3

    stop_threshold = 0.9
    draw_threshold = 0.7

    iterations = 0
    max_nb_iterations = 5

    best_results = []
    best_result_shape = (0,0)
    best_results_loc = (0,0)
    best_result = 0
    best_results_c = []
    best_result_shape_c = (0,0)
    best_results_loc_c = (0,0)
    best_result_c = 0


    while highest_value<stop_threshold and iterations<=max_nb_iterations:

        iterations += 1
        small_scale = downsize_factor * scale_highest_value
        big_scale = upsize_factor * scale_highest_value

        for scale in np.linspace(small_scale, big_scale, num=10):

            for rotation in np.linspace(-max_rotation, max_rotation, num=5):

                if(scale>= biggest_scale or scale<=smallest_scale):
                    continue

                new_width = nextOddNumber(w*scale)
                new_height = nextOddNumber(h*scale)
                new_shape = (new_width, new_height)
                resized = cv2.resize(template, new_shape, interpolation = cv2.INTER_AREA)
                resized = imutils.rotate(resized, rotation)

                new_width_c = nextOddNumber(w_c*scale)
                new_height_c = nextOddNumber(h_c*scale)
                new_shape_c = (new_width_c, new_height_c)
                resized_c = cv2.resize(template_counterclockwise, new_shape_c, interpolation = cv2.INTER_AREA)
                resized_c = imutils.rotate(resized_c, rotation)


                try:
                    res = cv2.matchTemplate(blackAndWhiteImage,resized,cv2.TM_CCOEFF_NORMED)
                    res_c = cv2.matchTemplate(blackAndWhiteImage,resized_c,cv2.TM_CCOEFF_NORMED)
                except Exception as e:
                    continue

                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                min_val_c, max_val_c, min_loc_c, max_loc_c = cv2.minMaxLoc(res_c)

                loc = np.where( res >= draw_threshold)
                loc_c = np.where( res_c >= draw_threshold)

                if(max_val>best_result):
                    if(max_val>highest_value):
                        highest_value = max_val
                        scale_highest_value = scale
                    best_result = max_val
                    best_results = res
                    best_result_shape = new_shape
                    best_results_loc = max_loc

                if(max_val_c>best_result_c):
                    if(max_val>highest_value):
                        highest_value = max_val_c
                        scale_highest_value = scale
                    best_result_c = max_val_c
                    best_results_c = res_c
                    best_result_shape_c = new_shape_c
                    best_results_loc_c = max_loc_c


    target_loc = (0,0)
    target_shape = (0,0)

    if(best_result>best_result_c):
        target_loc = best_results_loc
        target_shape = best_result_shape
    else:
        target_loc = best_results_loc_c
        target_shape = best_result_shape_c

    target_x = target_loc[0]+round(target_shape[0]/2)
    target_y = target_loc[1]+round(target_shape[1]/2)

    board_width_factor = 3.1
    left_x = target_x - round(board_width_factor*target_shape[0])
    right_x = target_x + round(board_width_factor*target_shape[0])
    top_y = target_y + round(board_width_factor*target_shape[1])
    bottom_y = target_y - round(board_width_factor*target_shape[1])

    board_crop = blackAndWhiteImage[bottom_y:top_y,left_x:right_x]

    board_correlation = np.zeros((5,5,4), dtype=float)

    w = target_shape[0]
    h = target_shape[1]


    resized = cv2.resize(template, target_shape, interpolation=cv2.INTER_AREA)
    resized_c = cv2.resize(template_counterclockwise, target_shape, interpolation=cv2.INTER_AREA)

    try:
        res = cv2.matchTemplate(board_crop, resized, cv2.TM_CCOEFF_NORMED)
    except Exception as e:
        pass

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    try:
        res_c = cv2.matchTemplate(board_crop, resized_c, cv2.TM_CCOEFF_NORMED)
    except Exception as e:
        pass

    min_val_c, max_val_c, min_loc_c, max_loc_c = cv2.minMaxLoc(res_c)


    board_crop_shape = board_crop.shape

    board_crop_center_x = round(board_crop_shape[0]/2)
    board_crop_center_y = round(board_crop_shape[1]/2)
    board_crop_center = (board_crop_center_x,board_crop_center_y)

    res_shape = res.shape
    results_center_x = round(res_shape[0]/2)
    results_center_y = round(res_shape[1]/2)
    results_center = (results_center_x,results_center_y)

    w_index = 0
    h_index = 0
    for h_offset in range(-2,3):
        w_index = 0
        for w_offset in range(-2,3):
            y_offset = h_offset*h + results_center_y
            x_offset = w_offset*w + results_center_x

            surrounding = round(h/3)
            res_val = maxValueInNeighborhood(res, (x_offset,y_offset),range_delta_x=surrounding,range_delta_y=surrounding)
            res_c_val = maxValueInNeighborhood(res_c, (x_offset,y_offset),range_delta_x=surrounding,range_delta_y=surrounding)

            board_correlation[h_index][w_index][0] = res_val
            board_correlation[h_index][w_index][1] = res_c_val

            #Nothing = 0
            #Clockwise = 1
            #Counterclockwise = 2
            most_likely_shape = 0
            most_likely_shape_value = 0

            if(res_val >res_c_val):
                most_likely_shape = 1
                most_likely_shape_value = res_val
            elif(res_c_val> res_val):
                most_likely_shape = 2
                most_likely_shape_value = res_c_val

            if(most_likely_shape_value<0.4):
                most_likely_shape = 0
                most_likely_shape_value = 0

            board_correlation[h_index][w_index][2] = most_likely_shape
            board_correlation[h_index][w_index][3] = most_likely_shape_value

            w_index+=1
        h_index+=1


    final_board = findPositionsInBoard(board_correlation)

    print("Board prediction")
    print("Black = 0")
    print("Clockwise = 1")
    print("Counterclockwise = 2")
    print(final_board)



