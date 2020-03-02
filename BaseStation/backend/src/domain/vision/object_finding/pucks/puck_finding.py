import cv2
import numpy as np
import src.domain.vision.image_processing as img_proc


class PuckColors(object):
    def __init__(self):

        self.red = PuckColor("red", (5, 150, 75), (177, 150, 75))
        self.orange = PuckColor("orange", (15, 135, 130))
        self.yellow = PuckColor("yellow", (25, 160, 160))
        self.green = PuckColor("green", (60, 140, 75))
        self.blue = PuckColor("blue", (110, 130, 70), (110, 180, 70))
        self.purple = PuckColor("purple", (160, 127, 127))
        self.gray = PuckColor("gray", (90, 130, 95))
        self.black = PuckColor("black", (90, 100, 50), (90, 180, 50))
        self.brown = PuckColor("brown", (127, 30, 40), (127, 130, 40))
        self.white = PuckColor("white", (100, 70, 160))
        self.colors = [self.red, self.orange, self.yellow, self.green, self.blue, self.purple, self.gray, self.black,
                       self.brown, self.white]
        # self.colors = []

    def get_color_scores(self, unknown_color):
        scores = {}
        for color in self.colors:
            scores[color.name] = color.get_score(unknown_color)

        return sorted(scores.items(), key=lambda kv: (kv[1], kv[0]))


class Puck(object):
    def __init__(self, x, y, color, color_average):
        self.x = x
        self.y = y
        self.color = color
        self.color_average = color_average


class PuckColor(object):
    def __init__(self, name, color, color2=None):
        self.name = name
        self.color = color
        self.color2 = color2

    def get_score(self, color):
        score = 0
        score += abs(color[0] - self.color[0])
        score += abs(color[1] - self.color[1])
        score += abs(color[2] - self.color[2])
        if self.color2 is not None:
            score2 = self.get_score2(color)
            score = min(score, score2)
        return score

    def get_score2(self, color):
        score = 0
        score += abs(color[0] - self.color2[0])
        score += abs(color[1] - self.color2[1])
        score += abs(color[2] - self.color2[2])
        return score


class PuckFinder(object):
    def __init__(self):
        self.puck_colors = PuckColors()
        self.pucks = []

    def find_pucks(self, image, debug=False):
        self.pucks = []
        ret_pucks = {}
        # ret_pucks_score = {}
        processed_image_sat = img_proc.saturation_multiplier(image, 3)
        processed_image_sat_open = img_proc.image_opening(processed_image_sat, kernel=np.ones((4, 4), np.uint8))
        image_edge = img_proc.edge_detection_bgr(processed_image_sat_open)
        if debug:
            cv2.imshow("edge", image_edge)
            cv2.imshow("processed_image", processed_image_sat_open)
        circles = cv2.HoughCircles(image_edge, cv2.HOUGH_GRADIENT, 1.6, 10, param1=40, param2=23,
                                   minRadius=10, maxRadius=14)
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for circle in circles[0, :]:
                if circle[2] != 0:  # if the radius (circle[2]) is not null
                    single_circle_image = img_proc.crop_image_circle(
                        processed_image_sat_open, x=circle[0], y=circle[1], radius=11
                    )
                    color_average = img_proc.average_image_color(single_circle_image)
                    colors_scores = self.puck_colors.get_color_scores(color_average)
                    self.pucks.append(Puck(x=circle[0], y=circle[1], color=colors_scores, color_average=color_average))

            self.__analyse_best_color_match()
            self.__analyse_best_color_match()
            self.__analyse_best_color_match()

            # for color in self.puck_colors.colors:
            #     ret_pucks_score[color.name] = 100000, None
            #

            # for puck in self.pucks:
            #     for puck_color_score in puck.color:
            #         if ret_pucks_score[puck_color_score[0]][0] > puck_color_score[1]:
            #             ret_pucks_score[puck_color_score[0]] = (puck_color_score[1], puck.color_average)
            #             ret_pucks[puck_color_score[0]] = {'x': puck.x, 'y': puck.y}
            # print(ret_pucks_score, ret_pucks)
            if debug:
                count = 0
                for puck in self.pucks:
                    print("{} - x = {}, y = {}, colors scores = {}, color average = {}".format(count, puck.x, puck.y,
                                                                                               puck.color,
                                                                                               puck.color_average))
                    cv2.putText(image, str(count) + "-" + str(puck.color[0][0]), (puck.x - 30, puck.y),
                                cv2.FONT_HERSHEY_COMPLEX, 0.3, (0, 255, 0))
                    cv2.imshow("image", image)
                    count += 1
            for puck in self.pucks:
                ret_pucks[puck.color[0][0]] = {'x': puck.x, 'y': puck.y}
            return ret_pucks

    def __analyse_best_color_match(self):
        for puck in self.pucks[:]:
            try:
                while not self.__puck_best_score_color(puck):
                    puck.color = puck.color[1:]
            except IndexError:
                # pass
                self.pucks.remove(puck)

    def __puck_best_score_color(self, puck):
        for other_puck in self.pucks:

            if other_puck != puck:
                if other_puck.color[0][0] == puck.color[0][0]:  # if puck best score color name match with other puck
                    if other_puck.color[0][1] < puck.color[0][1]:  # if other puck color score is better
                        return False
                    elif other_puck.color[0][1] == puck.color[0][1] and other_puck.color[1][1] > puck.color[1][1]:
                        # if other puck color score is equal and other puck color second color score is worst
                        return False

        return True
