from typing import List
from src.domain.vision.object_finding.ArucoMarkerFinder import ArucoMarkerFinder
from src.domain.vision.types import ArucoPosition


class PillarFinder:

    def __init__(self, aruco_marker_finder: ArucoMarkerFinder):
        self.__aruco_marker_finder = aruco_marker_finder

    def find_all(self, image) -> List[ArucoPosition]:
        # TODO filter with ids
        aruco_markers = self.__aruco_marker_finder.find_all(image)
        aruco_positions = self.__aruco_marker_finder.calculate_3d_positions(aruco_markers)
        return aruco_positions
