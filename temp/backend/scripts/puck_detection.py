import os
import cv2
from src.domain.vision.object_finding.pucks.puck_finding import PuckFinder


def photo_test(filename):
    frame = cv2.imread(filename)

    frame = frame[85:-75, 10:]
    puck_finder = PuckFinder()
    puck_finder.find_pucks(frame, debug=True)

    cv2.imshow("original", frame)

    cv2.waitKey(0)   # press enter to pass to the next image


if __name__ == '__main__':
    puckTestPhotos = os.listdir("PuckTestPhotos")
    for photo in puckTestPhotos:
        print("\n\nPuckTestPhotos/" + photo)
        photo_test("PuckTestPhotos/" + photo)  # press enter to pass to the next image
