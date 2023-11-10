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

    def __str__(self):
        """
        Returns information about a square object.

        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
