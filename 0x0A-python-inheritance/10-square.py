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
