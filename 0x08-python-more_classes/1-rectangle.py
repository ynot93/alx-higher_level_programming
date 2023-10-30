#!/usr/bin/python3
"""
This module defines an empty Recyangle class.

"""


class Rectangle:
    """
    This class defines a rectangle.

    """
    def __init__(self, width=0, height=0):
        """
        Initialize object with with attribute.

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter function to provide value of width.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter function to get vallue of width.
        
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Getter function to get the height value.

        """
        return self.__height

    @height.settter
    def height(self, value):
        """
        Setter function to set value of the height.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
