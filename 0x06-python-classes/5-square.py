#!/usr/bin/python3
"""This module performs calculations on a square"""


class Square:
    """Class that represents a square.

    Attributes:
        size (int): Size of the square

    """
    def __init__(self, size=0):
        """Initializes object with optional size.

        Args:
            size (int, optional): Size of the square, defaults to 0.

        """
        self.__size = size

    @property
    def size(self):
        """Get size of square.

        Returns:
            int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value(int): Size of the square.

        Raise:
            ValueError: if value < 0
            TypeError: if value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValuError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of the square.

        Return:
            int: area of the square.

        """
        return self.__size * seld.__size

    def my_print(self):
        """Print the square using #.

        If size = 0, print an empty line.

        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
