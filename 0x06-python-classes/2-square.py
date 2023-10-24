#!/usr/bin/python3
"""This is a module that performs operations on a square"""


class Square:
    """This is a class that defines a square.

    Attributes:
        size (int): The size of the square.

    """

    def __init__(self, size=0):
        """Initializes object of class Square with these attributes.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
