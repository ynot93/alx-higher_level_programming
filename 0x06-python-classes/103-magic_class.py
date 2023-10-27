#!/usr/bin/python3
"""Derive a class PythonClass from Python bytecode"""

import math


class MagicClass:
    """Defines the calculations done on a circle."""

    def __init__(self, radius=0):
        """Initializes a circle.

        Args:
            radius (int, float):  Radius of the circle. Initialized to 0.

        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """Calculates the area of a circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference of the circle."""
        return self.__radius * 2 * math.pi
