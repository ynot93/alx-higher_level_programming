#!/usr/bin/python3
"""
This module prints a square using '#' character.

"""


def print_square(size):
    """
    Prints a square.

    Args:
        size(int): The side length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        return

    for i in range(size):
        print("#" * size)
