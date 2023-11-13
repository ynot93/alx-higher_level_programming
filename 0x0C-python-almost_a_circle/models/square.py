#!/usr/bin/python3
"""
This module defines a square which inherits from class Rectangle.

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines a square object that inherits rectangle attributes
    and methods.

    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a square object with the following attributes.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter function for size of square.

        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Seter function for size of square.

        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns attributes to variable (key-word) arguments.

        """
        argmnts = ['id', 'size', 'x', 'y']

        if args:
            for i, arg in enumerate(args):
                setattr(self, argmnts[i], arg)

        else:
            for key, value in kwargs.items():
                if key in argmnts:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns dictionary representation of Square.

        """
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
        }

    def __str__(self):
        """
        Returns information about a square object.

        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
