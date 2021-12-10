#!/usr/bin/python3
""" Module that Holds Pascal's Triangle task
"""


def pascal_triangle(n):
    """ Function that returns a list of lists of integers
        representing the Pascal's triangle of n
    """
    pascalTri = []
    if n <= 0:
        return pascalTri
    for i in range(1, (n + 1)):
        array = []
        for j in range(i):
            array.append(1)
        pascalTri.append(array)
    for i in range(len(pascalTri)):
        for j in range(i):
            if j != 0:
                pascalTri[i][j] = pascalTri[i - 1][j] + pascalTri[i - 1][j - 1]
    return pascalTri
