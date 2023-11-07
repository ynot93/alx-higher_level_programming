#!/usr/bin/python3
"""
This is a module about Pascal's Triangle.

"""


def pascal_triangle(n):
    """
    Returns list of lists of integers representing Pascal's triangle.

    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        current_row = [1]
        for j in range(1, i):
            current_row.append(triangle[i-1][j-1] + triangle[i-1][j])
        current_row.append(1)

        triangle.append(current_row)

    return triangle
