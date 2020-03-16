import cv2
import numpy as np
from cv2 import aruco
from typing import List
from src.domain.vision.types import CameraCalibration, ArucoMarker, ArucoPosition


class ArucoMarkerFinder:
    def __init__(self, camera_calibration: CameraCalibration, marker_width: float, aruco_dict: int):
        self.__camera_calibration = camera_calibration
        self.__marker_width = marker_width
        self.__aruco_dict = aruco.Dictionary_get(aruco_dict)
        self.__aruco_parameters = aruco.DetectorParameters_create()

    def find_all(self, image) -> List[ArucoMarker]:
        grayscaled_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        corners, ids, rejectedImgPoints = aruco.detectMarkers(
            grayscaled_image,
            self.__aruco_dict,
            parameters=self.__aruco_parameters
        )

        if ids is None:
            return []

        aruco_markers = []

        for aruco_id, aruco_corners in zip(ids, corners):
            aruco_markers.append(ArucoMarker(aruco_id, aruco_corners))
            image = cv2.polylines(image, aruco_corners.astype(np.int32), True, (255, 0, 255), 2)

        return aruco_markers

    def calculate_3d_positions(self, aruco_markers: List[ArucoMarker]) -> List[ArucoPosition]:
        corners = [aruco_marker.corner for aruco_marker in aruco_markers]

        if len(corners) < 1:
            return []

        rotation_vectors, translation_vectors, objects_points = aruco.estimatePoseSingleMarkers(
            corners,
            self.__marker_width,
            self.__camera_calibration.camera_matrix,
            self.__camera_calibration.distortion_coefficients
        )

        aruco_positions = [
            ArucoPosition(
                object_points=object_points,
                rotation_vector=rotation_vector,
                translation_vector=translation_vector
            )
            for rotation_vector, translation_vector, object_points
            in zip(rotation_vectors, translation_vectors, objects_points)
        ]

        return aruco_positions
