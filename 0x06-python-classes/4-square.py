#!/usr/bin/python3
"""This module performs calculations on a square."""


class Square:
    """A class that represents a square.

    Attributes:
        size (int): Size of the square.

    """
    def __init__(self, size=0):
        """Initializes Square objects with these attributes.

        Args:
            size (int, optional): Size of the square. Initialized to 0.

        """
        self.__size = size

    @property
    def size(self):
        """Gets the size.

        Returns:
            The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size.

        Args:
            value (int): size of the square.

        Raise:
            ValueError: If size is less than zero.
            TypeError: If size is not an integer.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: Area of the square.

        """
        return self.__size * self.__size
