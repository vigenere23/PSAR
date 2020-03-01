import json
import numpy as np
from src.domain.vision.types import CameraCalibration


class CameraCalibrationRepository:
    def save_calibration(self, camera_calibration: CameraCalibration, calib_path: str):
        data = {
            'camera_matrix': camera_calibration.camera_matrix.tolist(),
            'distortion_coefficients': camera_calibration.distortion_coefficients.tolist()
        }

        with open(calib_path, 'w') as calib_file:
            calib_file.write(json.dumps(data))

    def load_calibration(self, calib_path: str) -> CameraCalibration:
        calib_file = open(calib_path, 'r')
        data = json.load(calib_file)
        return CameraCalibration(np.array(data['camera_matrix']), np.array(data['distortion_coefficients']))
