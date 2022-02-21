import numpy as np
import cv2
from pyramid import Pyramid


# FUNCTIONS
def draw_pyramid(img, pyramid, offset_left=0, offset_top=0):
    # edge color change
    pyramid.brightness += 8
    # if almost white
    if pyramid.brightness >= 255:
        pyramid.brightness = 0

    # take X, Y coord, apply offset and cast
    matrix = (pyramid.matrix[:, :2].copy() + np.array([offset_left, offset_top])).astype(np.int32)

    # split matrix
    top = matrix[0, :]
    matrix = matrix[1:, :]

    # from H to other
    for j in range(-1, matrix.shape[0] - 1):
        poly = np.concatenate((matrix[j:j+2], [top]), axis=0)
        cv2.fillPoly(img, [poly], (pyramid.brightness, pyramid.brightness, pyramid.brightness))

    # bottom square lines
    cv2.fillPoly(img, [matrix], (pyramid.brightness, pyramid.brightness, pyramid.brightness))


# CREATE PYRAMID
pyramid = Pyramid(50, 100)

# PRINT AND PLOT
while True:
    img = np.ones((480, 640, 3), dtype=np.uint8) * 255
    draw_pyramid(img, pyramid, offset_left=320, offset_top=240)
    cv2.imshow("Display", img)
    key = cv2.waitKey(0)
    print(key)
    # X
    if key == 120:
        pyramid.rotate_x(1)
    # Y
    if key == 121:
        pyramid.rotate_y(1)
    # Z
    if key == 122:
        pyramid.rotate_z(1)
    # Reset
    if key == 114:
        pyramid = Pyramid(50, 100)
    # End
    if key == -1:
        break
