import cv2
import numpy as np
from src.domain.vision.camera.Camera import Camera
from src.domain.vision.camera.Capture import Capture


class WorldCamera(Camera):
    __DEFAULT_FRAME_WIDTH = 1600
    __DEFAULT_ASPECT_RATIO = 1.6

    def __init__(self, device, frame_width=__DEFAULT_FRAME_WIDTH, aspect_ratio=__DEFAULT_ASPECT_RATIO):
        self.__device = device
        self.__camera = cv2.VideoCapture(device)
        self.__camera.set(cv2.CAP_PROP_BUFFERSIZE, 5)
        self.set_aspect_ratio(aspect_ratio)
        self.set_resolution(frame_width)

    def open(self):
        if not self.__camera.isOpened():
            self.__camera.open(self.__device)

    def ensure_open(self):
        if self.__camera.isOpened():
            self.close()

        while not self.__camera.isOpened():
            self.__camera.open(self.__device)

    def close(self):
        self.__camera.release()

    def capture(self) -> Capture:
        ret, image = self.__camera.read()
        return Capture(ret=ret, image=image)

    def ensure_capture(self) -> np.ndarray:
        ret, image = self.__camera.read()

        while not ret:
            self.ensure_open()
            ret, image = self.__camera.read()

        return image

    def set_resolution(self, frame_width=__DEFAULT_FRAME_WIDTH):
        self.__camera.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
        self.__camera.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_width / self.__aspect_ratio)

    def set_aspect_ratio(self, aspect_ratio=__DEFAULT_ASPECT_RATIO):
        self.__aspect_ratio = aspect_ratio
