#!/usr/bin/python3
"""
This module defines attributes of a square.

"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    """
    def __init__(self, size):
        """
        Initializes a Square object.

        """
        super().__init__(size, size)

    def __str__(self):
        """
        Returns object representation in string format.

        """
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
