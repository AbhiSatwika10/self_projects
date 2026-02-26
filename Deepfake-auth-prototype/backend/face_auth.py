import cv2
import numpy as np

stored = cv2.imread("models/stored.jpg", 0)


def simple_face_match(img):
    live = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    live = cv2.resize(live, (stored.shape[1], stored.shape[0]))

    diff = np.mean(cv2.absdiff(live, stored))

    if diff < 60:
        return True
    return False
