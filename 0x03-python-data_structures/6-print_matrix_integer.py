#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers"""
    if matrix is None:
        return None

    for item in matrix:
        row = ""
        for num in item:
            row += "{:d} ".format(num)
        print(row.strip())
