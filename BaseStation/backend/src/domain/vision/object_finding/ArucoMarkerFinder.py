import cv2
from cv2 import aruco
from typing import List
from src.domain.vision.types import CameraCalibration, ArucoMarker, ArucoPosition


class ArucoMarkerFinder:
    def __init__(self, camera_calibration: CameraCalibration, aruco_length: float):
        self.__camera_calibration = camera_calibration

        # TODO put in config file
        self.__aruco_length = aruco_length
        self.__aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
        self.__aruco_parameters = aruco.DetectorParameters_create()
        self.__axis_length = 100.0

    def find_all(self, image) -> List[ArucoMarker]:
        grayscaled_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        corners, ids, rejectedImgPoints = aruco.detectMarkers(
            grayscaled_image,
            self.__aruco_dict,
            parameters=self.__aruco_parameters
        )

        return [
            ArucoMarker(aruco_id, aruco_corners) for aruco_id, aruco_corners in zip(ids, corners)
        ]

    def calculate_3d_positions(self, aruco_markers: List[ArucoMarker]) -> List[ArucoPosition]:
        corners = [aruco_marker.corner for aruco_marker in aruco_markers]

        rotation_vectors, translation_vectors, _ = aruco.estimatePoseSingleMarkers(
            corners,
            self.__aruco_length,
            self.__camera_calibration.camera_matrix,
            self.__camera_calibration.distortion_coefficients
        )

        aruco_positions = [ArucoPosition(rotation_vector, translation_vector) for rotation_vector, translation_vector in zip(rotation_vectors, translation_vectors)]

        return aruco_positions

    def show_all_markers_axes(self, image, aruco_positions: List[ArucoPosition]):
        aruco_markers_image = image

        for aruco_position in aruco_positions:
            aruco_markers_image = aruco.drawAxis(
                aruco_markers_image,
                self.__camera_calibration.camera_matrix,
                self.__camera_calibration.distortion_coefficients,
                aruco_position.rotation_vector,
                aruco_position.translation_vector,
                self.__axis_length
            )

        cv2.imshow('Aruco markers axes', aruco_markers_image)
        cv2.waitKey(20000)
