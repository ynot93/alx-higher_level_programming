#!/usr/bin/python3
"""
This module deals with inheritance in classes.

"""
def is_kind_of_class(obj, a_class):
    """
    Returns True if object is an instance of a class, or a subclass
    that inherits from a superclass.

    """
    if isinstance(obj, a_class):
        return True
    return False
