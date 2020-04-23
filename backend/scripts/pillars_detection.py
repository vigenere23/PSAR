import cv2
# import glob
import src.domain.vision.image_drawing as image_drawing
from cv2 import aruco
from src.argparser import args
from src.domain.vision.calibration.CameraCalibrationRepository import CameraCalibrationRepository
from src.domain.vision.object_finding.ArucoMarkerFinder import ArucoMarkerFinder
from src.domain.vision.object_finding.pillars.PillarFinder import PillarFinder
from src.infrastructure.cameras.WorldCamera import WorldCamera


if __name__ == "__main__":
    WINDOW_NAME = "Live feed"
    ARUCO_MARKER_WIDTH = 70.0  # in mm
    ARUCO_DICT = aruco.DICT_4X4_50
    TABLE_NUMBER = args.table
    CAMERA_DEVICE = args.camera
    # CAMERA_DEVICE = './assets/videos/pillars/table1/moving_1600x1000.webm'
    IMAGE_WIDTH = 1600  # max 1600
    ASPECT_RATIO = 16 / 10  # 16:10
    IMAGE_DIMENSIONS = (IMAGE_WIDTH, int(IMAGE_WIDTH / ASPECT_RATIO))

    camera_calibration_repository = CameraCalibrationRepository()
    camera_calibration = camera_calibration_repository.load_calibration(TABLE_NUMBER).to_new_dimensions(IMAGE_WIDTH, IMAGE_WIDTH / ASPECT_RATIO)
    aruco_marker_finder = ArucoMarkerFinder(camera_calibration, ARUCO_MARKER_WIDTH, ARUCO_DICT)
    pillar_finder = PillarFinder(aruco_marker_finder)
    camera = WorldCamera(CAMERA_DEVICE, frame_width=IMAGE_WIDTH, aspect_ratio=ASPECT_RATIO)

    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # out = cv2.VideoWriter('./output.avi', fourcc, 10.0, IMAGE_DIMENSIONS)

    # images = iter((cv2.imread(filename) for filename in glob.glob('./assets/images/pillars/table1/*')))

    while True:
        frame = camera.ensure_capture()

        # Only if camera device is no a live feed
        # frame = cv2.resize(frame, IMAGE_DIMENSIONS, interpolation=cv2.INTER_CUBIC)
        # frame = next(images)

        cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(WINDOW_NAME, 1600, 1000)

        aruco_markers_positions = pillar_finder.find_all(frame)

        # TODO seems not needed... to verify (+ quite slow)
        # TODO check if should move before aruco finding
        # frame = cv2.undistort(frame, camera_calibration.camera_matrix, camera_calibration.distortion_coefficients)

        frame = image_drawing.draw_aruco_markers_axes(frame, aruco_markers_positions, camera_calibration)
        frame = image_drawing.draw_pillars_bases(frame, aruco_markers_positions, camera_calibration)

        # out.write(frame)

        cv2.imshow(WINDOW_NAME, frame)

        # cv2.waitKey(20000)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.close()
    # out.release()
    cv2.destroyAllWindows()
