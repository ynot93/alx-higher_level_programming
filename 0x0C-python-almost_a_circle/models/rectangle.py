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
            raise ValueError("width must be > 0")
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
            raise ValueError("height must be > 0")
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
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter function for y atrribute.

        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter function for y attribute.

        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates the area of the rectangle.

        """
        return self.width * self.height

    def display(self):
        """
        Prints rectangle instance with # character.

        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """
        Updates atrributes with variable and key/word arguments.

        """
        argmnts = ['id', 'width', 'height', 'x', 'y']

        if args:
            for i in range(min(len(args), len(argmnts))):
                setattr(self, argmnts[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in argmnts:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns dictionary representation of Rectangle.

        """
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
        }

    def __str__(self):
        """
        Return formatted string of rectangle instance.

        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}\
                - {self.width}/{self.height}"
