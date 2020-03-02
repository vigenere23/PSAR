from src.domain.vision.ImageProcessing import *
import numpy as np
import cv2
import math


class TableCalibration(object):
    def __init__(self):
        pass


class TableCropper(object):
    def __init__(self, corners):
        self.corners = corners
        self.corrections, self.height, self.width = self.get_destination_points(self.corners)

    @staticmethod
    def get_destination_points(corners, debug=False):
        """
        -Get destination points from corners of warped images
        -Approximating height and width of the rectangle: we take maximum of the 2 widths and 2 heights
        Args:
            corners: list
            debug: print debug info if true
        Returns:
            destination_corners: list
            height: int
            width: int
        """

        w1 = np.sqrt((corners[0]['x'] - corners[1]['x']) ** 2 + (corners[0]['y'] - corners[1]['y']) ** 2)
        w2 = np.sqrt((corners[2]['x'] - corners[3]['x']) ** 2 + (corners[2]['y'] - corners[3]['y']) ** 2)
        w = max(int(w1), int(w2))

        h1 = np.sqrt((corners[0]['x'] - corners[2]['x']) ** 2 + (corners[0]['y'] - corners[2]['y']) ** 2)
        h2 = np.sqrt((corners[1]['x'] - corners[3]['x']) ** 2 + (corners[1]['y'] - corners[3]['y']) ** 2)
        h = max(int(h1), int(h2))

        destination_corners = np.float32([(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)])
        if debug:
            print('\nThe destination points are: \n')
            for index, c in enumerate(destination_corners):
                character = chr(65 + index) + "'"
                print(character, ':', c)

            print('\nThe approximated height and width of the original image is: \n', (h, w))
        return destination_corners, h, w

    @staticmethod
    def unwarp(img, src, dst, debug=False):
        """
        Args:
            img: np.array
            src: list
            dst: list
            debug: show plt graph and print if true
        Returns:
            un_warped: np.array
        """
        src = np.array([[i['x'], i['y']] for i in src])

        h, w = img.shape[:2]
        H, _ = cv2.findHomography(src, dst, method=cv2.RANSAC, ransacReprojThreshold=3.0)
        if debug:
            print('\nThe homography matrix is: \n', H)
        un_warped = cv2.warpPerspective(img, H, (w, h), flags=cv2.INTER_LINEAR)

        # plot
        if debug:
            from matplotlib import pyplot as plt

            f, (ax1, ax2) = plt.subplots(1, 2)
            ax1.imshow(img)
            x = [src[0]['x'], src[2]['x'], src[3]['x'], src[1]['x'], src[0]['x']]
            y = [src[0]['y'], src[2]['y'], src[3]['y'], src[1]['y'], src[0]['y']]
            ax1.plot(x, y, color='yellow', linewidth=3)
            ax1.set_ylim([h, 0])
            ax1.set_xlim([0, w])
            ax1.set_title('Targeted Area in Original Image')
            ax2.imshow(un_warped)
            ax2.set_title('Unwarped Image')
            plt.show()
        return un_warped

    def crop(self, image):
        return self.unwarp(image, self.corners, self.corrections)[0:self.height, 0:self.width]
