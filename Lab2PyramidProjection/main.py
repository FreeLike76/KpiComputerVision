import numpy as np
import cv2
from pyramid import Pyramid


# FUNCTIONS
def draw_pyramid_lines(img, pyramid, offset_left=0, offset_top=0):
    # edge color change
    pyramid.edge_brightness += 8
    # if almost white
    if pyramid.edge_brightness >= 255 * 0.8:
        pyramid.edge_brightness = 0

    # bottom square
    square = pyramid.matrix[1:, :]
    # from H to other
    for j in range(0, square.shape[0]):
        cv2.line(img,
                 (int(pyramid.matrix[0, 0] + offset_left), int(pyramid.matrix[0, 1] + offset_top)),
                 (int(square[j, 0] + offset_left), int(square[j, 1] + offset_top)),
                 (pyramid.edge_brightness, pyramid.edge_brightness, pyramid.edge_brightness), 1)

    # bottom square lines
    for j in range(-1, square.shape[0] - 1):
        cv2.line(img,
                 (int(square[j, 0] + offset_left), int(square[j, 1] + offset_top)),
                 (int(square[j + 1, 0] + offset_left), int(square[j + 1, 1] + offset_top)),
                 (pyramid.edge_brightness, pyramid.edge_brightness, pyramid.edge_brightness), 1)


# CREATE PYRAMID
pyramid = Pyramid(50, 100)

# PRINT AND PLOT

while True:
    img = np.ones((480, 640, 3), dtype=np.uint8) * 255
    draw_pyramid_lines(img, pyramid, offset_left=320, offset_top=240)
    cv2.imshow("Display", img)
    key = cv2.waitKey(0)
    print(key)
    # X
    if key == 121:
        pyramid.rotate_x(1)
    # Y
    if key == 120:
        pyramid.rotate_y(1)
    if key == 122:
        pyramid.rotate_z(1)