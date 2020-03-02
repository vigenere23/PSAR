import cv2
import glob
from src.domain.vision.calibration.CameraCalibrator import CameraCalibrator
from src.domain.vision.calibration.CameraCalibrationRepository import CameraCalibrationRepository
from src.domain.vision.calibration.ImageUndistorder import ImageUndistorder

CHESSBOARD_ROWS = 7
CHESSBOARD_COLUMNS = 6
CHESSBOARD_SQUARE_LENGTH = 100.0  # in mm
# ARUCO_SQUARE_LENGTH = 7.5  # in mm
ARUCO_LENGTH = 57.5  # in mm


if __name__ == '__main__':
    camera_calibration_repository = CameraCalibrationRepository()

    try:
        camera_calibration = camera_calibration_repository.load_calibration('./src/config/calibrations/calib1.json')
    except Exception:
        camera_calibrator = CameraCalibrator(CHESSBOARD_ROWS, CHESSBOARD_COLUMNS, CHESSBOARD_SQUARE_LENGTH)
        camera_calibration = camera_calibrator.calibrate_camera('./assets/images/calib/*')
        camera_calibration_repository.save_calibration(camera_calibration, './src/config/calibrations/calib1.json')

    image_undistorder = ImageUndistorder(camera_calibration)
    image = cv2.imread(glob.glob('./assets/images/pillars/*')[0])
    image_undistorder.undistord_image(image, show_image=True)
