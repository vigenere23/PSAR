import cv2
import numpy as np


def edge_detection_canny(gray, sigma):
    v = np.median(gray)
    # ---- apply optimal Canny edge detection using the computed median----
    lower_thresh = int(max(0, (1.0 - sigma) * v))
    upper_thresh = int(min(255, (1.0 + sigma) * v))
    # Using the Canny filter
    return cv2.Canny(gray, lower_thresh, upper_thresh)


def saturation_multiplier(image_bgr, multiplier):
    image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
    (hue, saturation, value) = cv2.split(image_hsv)
    saturation = saturation * multiplier
    saturation = np.clip(saturation, 0, 255)
    image_hsv = cv2.merge([hue, saturation, value])
    return cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)


def image_opening(image, kernel):
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


def edge_detection_bgr(image_bgr):
    blue, green, red = cv2.split(image_bgr)

    edge_b = edge_detection_canny(blue, 0.33)
    edge_g = edge_detection_canny(green, 0.33)
    edge_r = edge_detection_canny(red, 0.33)
    edge = cv2.bitwise_or(edge_b, edge_g)
    return cv2.bitwise_or(edge, edge_r)


def find_table(image):
    ret, thresh = cv2.threshold(image, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh, 1, 2)
    for cnt in contours:
        perimeter = cv2.arcLength(cnt, True)
        print(perimeter)


def crop_image_circle(image, x, y, radius):
    rectX = (x - radius)
    rectY = (y - radius)
    return image[rectY:(rectY + 2 * radius), rectX:(rectX + 2 * radius)]


def average_image_color(image):
    height, width, _ = np.shape(image)

    # calculate the average color of each row of our image
    avg_color_per_row = np.average(image, axis=0)

    # calculate the averages of our rows
    avg_colors = np.average(avg_color_per_row, axis=0)

    bgr_color = np.array(avg_colors, dtype=np.uint8)

    hsv_color = cv2.cvtColor(np.uint8([[tuple([int(x) for x in bgr_color])]]), cv2.COLOR_BGR2HSV)[0][0]
    return hsv_color


def unique_count_app(a):
    colors, count = np.unique(a.reshape(-1,a.shape[-1]), axis=0, return_counts=True)
    return colors[count.argmax()]
