#!/usr/bin/python3
"""This is a module about calculations on a square."""


class Square:
    """A class to represent a square.

    Attributes:
        size (int): Size of the square.
        position (tuple): Position of the square.

    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with an optional size

        Args:
            size (int): Size of the square.
            position (tuple): Position of the square.

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square.

        Return:
            int: size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of size.

        Args:
            value (int): value to set the size to.

        Raise:
            ValueError: if value is less than zero.
            TypeError: If value is not an integer.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Get the position of the square.

        Return:
            tuple: position of the square.

        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the value of the position.

        Args:
            value (tuple): Position as a tuple of 2 positive integers.

        Raise:
            TypeError: If value is not a tuple of 2 positive integers.

        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square.

        Return:
            int: area of the square.

        """
        return self.__size * self.__size

    def my_print(self):
        """Print square using '#'.

        If size is 0, print empty line

        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
