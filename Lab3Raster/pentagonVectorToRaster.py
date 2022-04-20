import numpy as np
import matplotlib.pyplot as plt
import math


# FUNCTIONS

def draw_figure(matrix):
    for point in range(-1, matrix.shape[1] - 1):
        draw_line(int(matrix[0, point]), int(matrix[1, point]),
                  int(matrix[0, point + 1]), int(matrix[1, point + 1]))


def draw_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
    sign_y = 1 if dy > 0 else -1 if dy < 0 else 0
    if dx < 0:
        dx = -dx
    if dy < 0:
        dy = -dy
    if dx > dy:
        pdx, pdy = sign_x, 0
        es, el = dy, dx
    else:
        pdx, pdy = 0, sign_y
        es, el = dx, dy
    x, y = x1, y1
    error, t = el / 2, 0

    xs = [x]
    ys = [y]

    while t < el:
        error -= es
        if error < 0:
            error += el
            x += sign_x
            y += sign_y
        else:
            x += pdx
            y += pdy
        t += 1

        xs.append(x)
        ys.append(y)

    plt.scatter(xs, ys, c=[[point_c / len(xs) for _ in range(3)] for point_c in range(len(xs))])


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
for i in range(5):
    temp = np.dot(rotate_matrix(20), temp)
    print("Pentagon:\n", temp)
    draw_figure(temp)
    plt.xlim([-200, 200])
    plt.ylim([-200, 200])
    plt.show()

temp = pentagon.copy()
for i in range(5):
    temp = np.dot(scale_matrix(1.2), temp)
    print("Pentagon:\n", temp)
    draw_figure(temp)
    plt.xlim([-200, 200])
    plt.ylim([-200, 200])
    plt.show()

temp = pentagon.copy()
for i in range(5):
    temp = temp + translate_matrix(20)
    print("Pentagon:\n", temp)
    draw_figure(temp)
    plt.xlim([-200, 200])
    plt.ylim([-200, 200])
    plt.show()
