import cv2
import glob
import numpy as np
from src.domain.vision.types import CameraCalibration

_DEFAULT_TERMINATION_CRITERIA = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)


class CameraCalibrator:

    def __init__(self, n_chessboard_rows: int, n_chessboard_columns: int, chessboard_square_length: float, termination_criteria=_DEFAULT_TERMINATION_CRITERIA):
        self.__n_chessboard_rows = n_chessboard_rows
        self.__n_chessboard_columns = n_chessboard_columns
        self.__chessboard_square_length = chessboard_square_length
        self.__termination_criteria = termination_criteria
        self.__known_board_positions = self.__create_known_board_positions()

    def calibrate_camera(self, calibration_images_path: str) -> CameraCalibration:
        image_space_chessboards_corners = self.get_image_space_chessboards_corners(calibration_images_path)
        all_known_board_positions = [self.__known_board_positions for i in range(len(image_space_chessboards_corners))]
        image_size = cv2.imread(glob.glob(calibration_images_path)[0]).shape[1::-1]
        # (corners_founded), camera_matrix, distortion_coefficients, (rotation_vectors, translation_vectors)
        camera_matrix, distortion_coefficients, rotation_vectors, translation_vectors = cv2.calibrateCamera(
            all_known_board_positions, image_space_chessboards_corners, image_size, None, None
        )[1:]

        calibration_error = self.__calculate_error(
            all_known_board_positions,
            image_space_chessboards_corners,
            rotation_vectors,
            translation_vectors,
            camera_matrix,
            distortion_coefficients
        )

        return CameraCalibration(
            aspect_ratio=float(image_size[0]) / float(image_size[1]),
            camera_matrix=camera_matrix,
            distortion_coefficients=distortion_coefficients,
            error=calibration_error,
            image_width=image_size[0],
            image_height=image_size[1]
        )

    def __create_known_board_positions(self):
        # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(ROWS-1,COLUMNS-1,0)
        board_positions = np.array([
            [i, j, 0] for j in range(self.__n_chessboard_columns) for i in range(self.__n_chessboard_rows)
        ], dtype=np.float32) * self.__chessboard_square_length
        return board_positions

    def __calculate_error(self, object_points, image_points, rotation_vectors, translation_vectors, camera_matrix, distortion_coefficients):
        total_error = 0

        for i in range(len(object_points)):
            image_points_2, _ = cv2.projectPoints(
                object_points[i],
                rotation_vectors[i],
                translation_vectors[i],
                camera_matrix,
                distortion_coefficients
            )
            error = cv2.norm(image_points[i], image_points_2, cv2.NORM_L2) / len(image_points_2)
            total_error += error

        return total_error / len(object_points)

    def get_image_space_chessboards_corners(self, calibration_images_path, show_images=False):
        image_space_chessboards_corners = []
        filenames = glob.glob(calibration_images_path)

        for filename in filenames:
            image = cv2.imread(filename)
            grayscaled_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            corners_founded, corners = cv2.findChessboardCorners(grayscaled_image, (self.__n_chessboard_rows, self.__n_chessboard_columns), None)

            if corners_founded:
                corners_with_better_accuracy = cv2.cornerSubPix(grayscaled_image, corners, (11, 11), (-1, -1), self.__termination_criteria)
                image_space_chessboards_corners.append(corners_with_better_accuracy)

                if show_images:
                    self.draw_chessboard_corners(image, corners_with_better_accuracy)

        return image_space_chessboards_corners

    def draw_chessboard_corners(self, chessboard_image, chessboard_corners):
        image = cv2.drawChessboardCorners(chessboard_image, (self.__n_chessboard_rows, self.__n_chessboard_columns), chessboard_corners, True)
        cv2.imshow('Chessboard corners', image)
        cv2.waitKey(5000)
