#!/usr/bin/python3
"""
This module deals with the Base class which will be imported
by all other classes in this project.

"""


class Base:
    """
    This class manages id attribute in all future classes.

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes objects of this class with an integer id.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
