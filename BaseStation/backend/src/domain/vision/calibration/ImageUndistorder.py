import cv2
from src.domain.vision.types import CameraCalibration


class ImageUndistorder:
    def __init__(self, camera_calibration: CameraCalibration):
        self.__camera_calibration = camera_calibration

    def undistord_image(self, image, show_image=False):
        undistorded_image = cv2.undistort(
            image,
            self.__camera_calibration.camera_matrix,
            self.__camera_calibration.distortion_coefficients
        )

        if show_image:
            cv2.imshow('Undistorded image', undistorded_image)
            cv2.waitKey(20000)
            cv2.destroyAllWindows()

        return undistorded_image
