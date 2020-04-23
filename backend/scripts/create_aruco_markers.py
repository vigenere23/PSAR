import cv2
from cv2 import aruco


if __name__ == '__main__':
    ARUCO_DICT = aruco.Dictionary_get(aruco.DICT_4X4_50)
    DIMENSION = 1000  # in pixels

    for i in range(3):
        image = aruco.drawMarker(ARUCO_DICT, i, DIMENSION)
        cv2.imwrite(f'./assets/images/aruco_markers/{i}.png', image)
