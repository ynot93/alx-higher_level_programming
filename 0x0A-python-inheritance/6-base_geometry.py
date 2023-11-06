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
