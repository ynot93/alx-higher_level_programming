#!/usr/bin/python3
"""
This module deals with inheritance of class Rectangle from
superclass BaseGeommetry.

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines attributes of a rectangle.

    """
    def __init__(self, width, height):
        """
        Initializes width and height attributes.

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Implements area of a Rectangle.

        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return Rectangle description.

        """
        return f"[Rectangle] {self.__width}/{self.__height}"
