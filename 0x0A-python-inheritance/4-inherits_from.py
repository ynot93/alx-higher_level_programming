#!/usr/bin/python3
"""
This module deals with classes and subclasses.

"""


def inherits_from(obj, a_class):
    """
    Returns True if object is an instance of a class that inherited
    from the specified class.

    """
    return issubclass(type(obj), a_class)
