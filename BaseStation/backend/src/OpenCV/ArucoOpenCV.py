import numpy as np
import cv2, PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import math

def generate_aruco(nx, ny):
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)

    fig = plt.figure()
    for i in range(1, nx * ny + 1):
        ax = fig.add_subplot(ny, nx, i)
        img = aruco.drawMarker(aruco_dict, i, 700)
        plt.imshow(img, cmap=mpl.cm.gray, interpolation="nearest")
        ax.axis("off")
        ax.set_title(i)

    plt.savefig("markers.pdf")
    plt.show()


def analyse_and_decode_aruco(filename):
    frame = cv2.imread(filename)
    plt.figure()
    plt.imshow(frame)
    plt.show()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters = aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)
    plt.figure()
    plt.imshow(frame_markers)
    ids = sorted(ids)
    for i in range(len(ids)):
        c = corners[i][0]
        print(corners[i][0][0][0])
        # plt.plot()
        plt.plot(corners[i][0][0][0], corners[i][0][0][1], ".")
        plt.plot([c[:, 0].mean()], [c[:, 1].mean()], "o", label="id={}, angle={}".format(ids[i],
                                                                                         round(math.degrees(math.atan2([c[:, 0].mean()] - corners[i][0][0][0],
                                                                                                    [c[:, 1].mean()] - corners[i][0][0][1])))))
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # generate_aruco(4, 3)
    # analyse_and_decode_aruco("aruco_marker_photo.jpg")
    analyse_and_decode_aruco("aruco_marker_photo_rotate.jpg")
