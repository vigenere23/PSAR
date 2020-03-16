import cv2
import glob
import src.domain.vision.image_processing as image_processing
from src.argparser import args
from src.domain.vision.calibration.CameraCalibrator import CameraCalibrator
from src.domain.vision.calibration.CameraCalibrationRepository import CameraCalibrationRepository


if __name__ == '__main__':
    CHESSBOARD_ROWS = 7
    CHESSBOARD_COLUMNS = 6
    CHESSBOARD_SQUARE_LENGTH = 100.0  # in mm
    TABLE_NUMBER = args.table

    camera_calibration_repository = CameraCalibrationRepository()

    try:
        camera_calibration = camera_calibration_repository.load_calibration(TABLE_NUMBER)
    except Exception:
        camera_calibrator = CameraCalibrator(CHESSBOARD_ROWS, CHESSBOARD_COLUMNS, CHESSBOARD_SQUARE_LENGTH)
        camera_calibration = camera_calibrator.calibrate_camera(f'./assets/images/calib/table{TABLE_NUMBER}/*')
        camera_calibration_repository.save_calibration(camera_calibration, TABLE_NUMBER)

    print(f'Calibration error : {camera_calibration.error}')
    print('Showing image undistortion...')

    image = cv2.imread(glob.glob(f'./assets/images/calib/table{TABLE_NUMBER}/*')[0])
    undistorded_image = image_processing.undistord_image(image, camera_calibration)

    cv2.imshow('Original image', image)
    cv2.imshow('Undistorded image', undistorded_image)
    cv2.waitKey(20000)
    cv2.destroyAllWindows()
