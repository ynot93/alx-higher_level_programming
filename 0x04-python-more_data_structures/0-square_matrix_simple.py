#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square of all integers of a matrix"""
    squared_matrix = []
    for item in matrix:
        squared = map(lambda x: x**2, item)
        squared_row = list(squared)
        squared_matrix.append(squared_row)
    return squared_matrix
