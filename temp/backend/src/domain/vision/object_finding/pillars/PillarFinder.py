import numpy as np
from typing import List
from src.domain.vision.object_finding.ArucoMarkerFinder import ArucoMarkerFinder
from src.domain.vision.types import ArucoPosition


class PillarFinder:

    __PILLAR_HEIGHT = 410.0  # in mm

    def __init__(self, aruco_marker_finder: ArucoMarkerFinder):
        self.__aruco_marker_finder = aruco_marker_finder

    def find_all(self, image) -> List[ArucoPosition]:
        # TODO filter with ids
        aruco_markers = self.__aruco_marker_finder.find_all(image)
        aruco_positions = self.__aruco_marker_finder.calculate_3d_positions(aruco_markers)

        for aruco_position in aruco_positions:
            aruco_position.object_points = np.array([[0.0, 0.0, self.__PILLAR_HEIGHT]])
            aruco_position.rotation_vector = np.array([[0.0, 0.0, 0.0]])

        return aruco_positions
