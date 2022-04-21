import numpy as np
import math


class Pyramid:
    def __init__(self, a, h):
        self.a = a
        self.h = h
        self.matrix = np.array([[0, 0, self.h, 0],  # H
                                [self.a, self.a, 0, 0],  # A
                                [-self.a, self.a, 0, 0],  # B
                                [-self.a, -self.a, 0, 0],  # C
                                [self.a, -self.a, 0, 0]])  # D

    def rotate_x(self, angle):
        rotate = np.array([[1, 0, 0, 0],
                           [0, math.cos(math.radians(angle)), -math.sin(math.radians(angle)), 0],
                           [0, math.sin(math.radians(angle)), math.cos(math.radians(angle)), 0],
                           [0, 0, 0, 1]])
        self.matrix = np.dot(self.matrix, rotate)

    def rotate_y(self, angle):
        rotate = np.array([[math.cos(math.radians(angle)), 0, math.sin(math.radians(angle)), 0],
                           [0, 1, 0, 0],
                           [-math.sin(math.radians(angle)), 0, math.cos(math.radians(angle)), 0],
                           [0, 0, 0, 1]])
        self.matrix = np.dot(self.matrix, rotate)

    def rotate_z(self, angle):
        rotate = np.array([[math.cos(math.radians(angle)), -math.sin(math.radians(angle)), 0, 0],
                           [math.sin(math.radians(angle)), math.cos(math.radians(angle)), 0, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]])
        self.matrix = np.dot(self.matrix, rotate)