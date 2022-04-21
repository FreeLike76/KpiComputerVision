import numpy as np
import matplotlib.pyplot as plt
from pyramid import Pyramid


# FUNCTIONS
def draw_pyramid(pyramid, xlim=(-256, 256), ylim=(-256, 256)):
    # split matrix
    top = pyramid.matrix[0, :2].astype(np.int32)
    bottom = pyramid.matrix[1:, :2].astype(np.int32)

    for j in range(-1, bottom.shape[0] - 1):
        # connecting two adj bottom points
        draw_line(bottom[j, 0], bottom[j, 1], bottom[j + 1, 0], bottom[j + 1, 1])
        # from one bottom point to top
        draw_line(bottom[j, 0], bottom[j, 1], top[0], top[1])

    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.show()


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
    # scatter points and use a gradient coloring
    plt.scatter(xs, ys, c=[[abs(point_c / len(xs) - 0.5) for _ in range(3)] for point_c in range(len(xs))])


# CREATE PYRAMID
pyramid = Pyramid(50, 100)
draw_pyramid(pyramid)

for i in range(3):
    pyramid.rotate_x(15)
    draw_pyramid(pyramid)

pyramid = Pyramid(50, 100)
for i in range(3):
    pyramid.rotate_y(15)
    draw_pyramid(pyramid)

pyramid = Pyramid(50, 100)
for i in range(3):
    pyramid.rotate_z(15)
    draw_pyramid(pyramid)

