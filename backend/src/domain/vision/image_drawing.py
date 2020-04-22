import cv2
import numpy as np
from cv2 import aruco
from typing import List
from src.domain.vision.types import ArucoPosition, CameraCalibration


def draw_pillars_bases(image: np.ndarray, aruco_markers_positions: List[ArucoPosition], camera_calibration: CameraCalibration):
    STANDARD_IMAGE_WIDTH = 1600
    STANDARD_PILLAR_PIXELS = 46

    image_copy = image.copy()
    pillar_pixels = int(STANDARD_PILLAR_PIXELS / STANDARD_IMAGE_WIDTH * camera_calibration.image_width)

    for aruco_markers_position in aruco_markers_positions:
        image_point, _ = cv2.projectPoints(
            aruco_markers_position.object_points,
            aruco_markers_position.rotation_vector,
            aruco_markers_position.translation_vector,
            camera_calibration.camera_matrix,
            camera_calibration.distortion_coefficients
        )
        image_point = tuple(image_point.reshape(2,).astype(np.int32))
        image_copy = cv2.circle(image_copy, image_point, pillar_pixels, (0, 255, 255), 2)

    return image_copy


def draw_aruco_markers_axes(image: np.ndarray, aruco_markers_positions: List[ArucoPosition], camera_calibration: CameraCalibration):
    AXIS_LENGTH = 100.0
    aruco_markers_image = image.copy()

    for aruco_position in aruco_markers_positions:
        aruco_markers_image = aruco.drawAxis(
            aruco_markers_image,
            camera_calibration.camera_matrix,
            camera_calibration.distortion_coefficients,
            aruco_position.rotation_vector,
            aruco_position.translation_vector,
            AXIS_LENGTH
        )

    return aruco_markers_image
