import json
import numpy as np
from src.domain.vision.types import CameraCalibration


class CameraCalibrationRepository:

    __BASE_PATH = './src/config/calibrations'

    def save_calibration(self, camera_calibration: CameraCalibration, table_number: int):
        data = camera_calibration.__dict__.copy()
        data['camera_matrix'] = data['camera_matrix'].tolist()
        data['distortion_coefficients'] = data['distortion_coefficients'].tolist()
        calib_path = self.__get_path(table_number)

        with open(calib_path, 'w') as calib_file:
            calib_file.write(json.dumps(data, sort_keys=True, indent=4))

    def load_calibration(self, table_number: int) -> CameraCalibration:
        calib_path = self.__get_path(table_number)
        calib_file = open(calib_path, 'r')
        data = json.load(calib_file)
        data['camera_matrix'] = np.array(data['camera_matrix'])
        data['distortion_coefficients'] = np.array(data['distortion_coefficients'])
        return CameraCalibration(**data)

    def __get_path(self, table_number: int):
        return f'{self.__BASE_PATH}/table{table_number}.json'
