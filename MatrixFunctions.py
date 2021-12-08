import numpy as np
from numpy import *
import math


def calculate_distance(p1, p2):
    i = 0
    distance = 0
    for i in range(len(p1)):
        distance += (p2[i] - p1[i]) ** 2
    return math.sqrt(distance)
# print(calculate_distance(array([1,1]),array([4,5])))


def determine_matrix_type(m):
    if m.ndim != 2:
        print(-1)
    else:
        for i in range(len(m)):
            if len(m[i]) != len(m[0]):
                print(0)
                return
        if len(m[0]) == len(m):
            print(2)
        else:
            print(1)
#determine_matrix_type(matrix([[1,2,7],[2,3,5],[8,40,8]]))


def transpose(n):
    if determine_matrix_type(n) == 1 or 2:
        n1 = n
        flat = [[n1[a][b] for a in range(len(n))] for b in range(len(n1[0]))]
        for row in flat:
            print(row)
#transpose(array([[1,2],[2,3],[8,40]]))


def spiral(n):
    up = 0
    down = n - 1
    right = n - 1
    left = 0
    m = n**2
    mtrx = np.zeros((n, n))
    if n//2 == 0:
        print(n + " is not an odd number")
    else:
        while m != 0:
            # down
            for i in range(up, down + 1):
                if m == 0:
                    break
                mtrx[i][left] = m
                m -= 1

            left += 1

            # right
            for j in range(left, right + 1):
                if m == 0:
                    break
                mtrx[down][j] = m
                m -= 1

            down -= 1

            # up
            for i in range(down, up - 1, -1):
                if m == 0:
                    break
                mtrx[i][right] = m
                m -= 1

            right -= 1

            # left
            for j in range(right, left - 1, -1):
                if m == 0:
                    break
                mtrx[up][j] = m
                m -= 1

            up += 1

        print(mtrx)

#spiral(5)


def write_in_a_file(mtx, path):
    for row in mtx:
        np.savetxt(path, mtx, fmt="%s")


def load_matrix_from_file(path):
    with open(path) as f:
        contents = f.read()
        print(contents)

#write_in_a_file([[1, 8], [3, 5]], "aper.txt")
#load_matrix_from_file("aper.txt")