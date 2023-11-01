#!/usr/bin/python3
"""
This module divides all elements in a matrix.

"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number

    Args:
        matrix: List of lists containing values.
        div(int or float): Divisor which cannot be zero.

    Return:
        matrix: With elements divide by 0 rounded to 2dp.

    Raises:
        TypeError: If matrix is not list of lists or
        if elements are not integer or float.
        TypeError: If rows of matrix have different sizes.
        TypeError: If 'div' is not integer or float.
        ZeroDivisionError: If 'div' is 0.

    """
    if not all(
            isinstance(row, list) and
            all(isinstance(item, (int, float)) for item in row)
            for row in matrix
    ):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    row_len = set(len(row) for row in matrix)
    if len(row_len) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(item / div, 2) for item in row] for row in matrix]

    return result
