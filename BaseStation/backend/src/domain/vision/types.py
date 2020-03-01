import numpy as np
from dataclasses import dataclass


@dataclass
class ArucoMarker:
    id: int
    corner: np.ndarray


@dataclass
class ArucoPosition:
    rotation_vector: np.ndarray
    translation_vector: np.ndarray


@dataclass
class CameraCalibration:
    camera_matrix: np.ndarray
    distortion_coefficients: np.ndarray
