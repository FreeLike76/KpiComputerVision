import numpy as np
import cv2
import math


# FUNCTIONS

def draw_point_matrix(img, matrix, offset_x=256, offset_y=256):
    for i in range(-1, matrix.shape[1] - 1):
        cv2.line(img,
                 (int(matrix[0, i] + offset_x), int(matrix[1, i] + offset_y)),
                 (int(matrix[0, i + 1] + offset_x), int(matrix[1, i + 1] + offset_y)),
                 (0, 0, 0), 1)

    cv2.imshow("Display", img)
    cv2.waitKey(500)


def rotate_matrix(angle):
    return np.array([[math.cos(math.radians(angle)), -math.sin(math.radians(angle))],
                     [math.sin(math.radians(angle)), math.cos(math.radians(angle))]])


def scale_matrix(coef):
    return np.array([[coef, 0],
                     [0, coef]])

def translate_matrix(coef):
    return np.array([[coef],
                     [coef]])

# CREATE PENTAGON MATRIX


outer_radius = 128
edges = 5
pentagon = np.zeros((2, edges), dtype=np.float32)
for i in range(0, edges):
    angle = i * 360 / edges
    pentagon[0, i] = outer_radius * math.cos(math.radians(angle))
    pentagon[1, i] = outer_radius * math.sin(math.radians(angle))

# PRINT

temp = pentagon.copy()
img = np.ones((512, 512, 3), dtype=np.uint8) * 255
for i in range(5):
    temp = np.dot(rotate_matrix(10), temp)
    print("Pentagon:\n", temp)
    draw_point_matrix(img, temp)

temp = pentagon.copy()
img = np.ones((512, 512, 3), dtype=np.uint8) * 255
for i in range(5):
    temp = np.dot(scale_matrix(1.1), temp)
    print("Pentagon:\n", temp)
    draw_point_matrix(img, temp)

temp = pentagon.copy()
img = np.ones((512, 512, 3), dtype=np.uint8) * 255
for i in range(5):
    temp = temp + translate_matrix(32)
    print("Pentagon:\n", temp)
    draw_point_matrix(img, temp)
