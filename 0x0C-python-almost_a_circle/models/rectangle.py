#!/usr/bin/python3
"""
This module deals with methods and attributes of the
class Rectangle.

"""
from models.base import Base


class Rectangle(Base):
    """
    Class rectangle inherits from base and has the
    following attributes.

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor that initializes a rectangle object with the attributes
        width, height, x, y and id.

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter function for width atrribute.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter function for width attribute.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("value must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter function for height atrribute.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter function for height attribute.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("value must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter function for x atrribute.

        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter function for x attribute.

        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        self.__x = value

    @property
    def y(self):
        """
        Getter function for y atrribute.

        """
        return self.__y

    @x.setter
    def y(self, value):
        """
        Setter function for y attribute.

        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        self.__y = value
