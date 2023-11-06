#!/usr/bin/python3
"""
This module deals with a geometry superclass and its modules,
attributes and subclasses.

"""


class BaseGeometry:
    """
    Defines a superclass called BaseGeometry.

    """
    def area(self):
        """
        Calculates the area of a geometric shape

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates data type of <name>

        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
