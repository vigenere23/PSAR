import numpy as np
from dataclasses import dataclass


@dataclass
class ArucoMarker:
    id: int
    corner: np.ndarray


@dataclass
class ArucoPosition:
    object_points: np.ndarray
    rotation_vector: np.ndarray
    translation_vector: np.ndarray


@dataclass
class CameraCalibration:
    image_width: int
    image_height: int
    aspect_ratio: float
    camera_matrix: np.ndarray
    distortion_coefficients: np.ndarray
    error: float

    def to_new_dimensions(self, new_image_width: int, new_image_height: int):
        new_camera_calibration = CameraCalibration(**self.__dict__.copy())

        new_camera_calibration.camera_matrix[0] *= new_image_width / self.image_width
        new_camera_calibration.camera_matrix[1] *= new_image_height / self.image_height

        new_camera_calibration.image_width = new_image_width
        new_camera_calibration.image_height = new_image_height
        new_camera_calibration.aspect_ratio = new_image_width / new_image_height

        return new_camera_calibration
