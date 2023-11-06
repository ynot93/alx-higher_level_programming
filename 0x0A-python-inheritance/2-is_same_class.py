#!/usr/bin/python3
"""
This module deals with classes and their instances.

"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is an exact instance of the class,
    otherwise it returns False.

    """
    return type(obj) is a_class
