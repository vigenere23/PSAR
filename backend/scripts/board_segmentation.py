import cv2
import numpy as np

if __name__ == '__main__':

    board_path = './assets/images/boards/arrows/10004.jpg'

    img = cv2.imread(board_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    low_hsv = np.array([0, 40, 40])
    high_hsv = np.array([255, 255, 255])
    mask1 = cv2.inRange(img, low_hsv, high_hsv)

    k_size = 20
    kernel = np.ones((k_size, k_size), np.uint8)
    opened = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, kernel)

    k_size = 10
    kernel = np.ones((k_size, k_size), np.uint8)
    opened = cv2.erode(opened, kernel, iterations=2)

    k_size = 20
    kernel = np.ones((k_size, k_size), np.uint8)
    opened = cv2.morphologyEx(opened, cv2.MORPH_OPEN, kernel)

    opened = cv2.bitwise_not(opened)

    res1 = cv2.bitwise_and(img, img, mask=opened)

    cv2.imwrite('./assets/images/boards/arrows/output.png', res1)
