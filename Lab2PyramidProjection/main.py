import numpy as np
import cv2
import math


# FUNCTIONS

def draw_pyramid_lines(img, matrix, offset_left=0, offset_top=0):
    # bottom square
    square = matrix[1:, :]

    # from H to other
    for j in range(0, square.shape[0]):
        cv2.line(img,
                 (int(matrix[0, 0] + offset_left), int(matrix[0, 1] + offset_top)),
                 (int(square[j, 0] + offset_left), int(square[j, 1] + offset_top)),
                 (0, 0, 0), 1)

    # bottom square lines
    for j in range(-1, square.shape[0] - 1):
        cv2.line(img,
                 (int(square[j, 0] + offset_left), int(square[j, 1] + offset_top)),
                 (int(square[j + 1, 0] + offset_left), int(square[j + 1, 1] + offset_top)),
                 (0, 0, 0), 1)


def rotate_matrix_x(angle):
    return np.array([[1, 0, 0, 0],
                     [0, math.cos(math.radians(angle)), math.sin(math.radians(angle)), 0],
                     [0, -math.sin(math.radians(angle)), math.cos(math.radians(angle)), 0],
                     [0, 0, 0, 1]])


def rotate_matrix_y(angle):
    return np.array([[math.cos(math.radians(angle)), 0, -math.sin(math.radians(angle)), 0],
                     [0, 1, 0, 0],
                     [math.sin(math.radians(angle)), 0, math.cos(math.radians(angle)), 0],
                     [0, 0, 0, 1]])


# CREATE PYRAMID
pyramid_a = 50
pyramid_h = 200
pyramid = np.array([[0, 0, pyramid_h, 0],  # H
                    [pyramid_a, pyramid_a, 0, 0],  # A
                    [-pyramid_a, pyramid_a, 0, 0],  # B
                    [-pyramid_a, -pyramid_a, 0, 0],  # C
                    [pyramid_a, -pyramid_a, 0, 0]])  # D

# PRINT AND PLOT

while True:
    img = np.ones((480, 640, 3), dtype=np.uint8) * 255
    print("Pyramid:\n", pyramid)
    draw_pyramid_lines(img, pyramid, offset_left=320, offset_top=240)
    cv2.imshow("Display", img)
    key = cv2.waitKey(0)
    # X
    if key == 121:
        pyramid = np.dot(pyramid, rotate_matrix_x(1))
    # Y
    if key == 120:
        pyramid = np.dot(pyramid, rotate_matrix_y(1))
