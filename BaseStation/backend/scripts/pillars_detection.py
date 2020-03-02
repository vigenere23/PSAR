import cv2
import glob
from src.domain.vision.calibration.CameraCalibrator import CameraCalibrator
from src.domain.vision.calibration.CameraCalibrationRepository import CameraCalibrationRepository
from src.domain.vision.object_finding.ArucoMarkerFinder import ArucoMarkerFinder
from src.domain.vision.object_finding.pillars.PillarFinder import PillarFinder

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

    aruco_marker_finder = ArucoMarkerFinder(camera_calibration, ARUCO_LENGTH)
    pillar_finder = PillarFinder(aruco_marker_finder)

    for filename in glob.glob('./assets/images/pillars/*'):
        pillar_image = cv2.imread(filename)
        aruco_markers_positions = pillar_finder.find_all(pillar_image)
        aruco_marker_finder.show_all_markers_axes(pillar_image, aruco_markers_positions)
