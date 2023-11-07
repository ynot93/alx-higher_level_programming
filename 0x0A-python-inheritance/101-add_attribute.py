#!/usr/bin/python3
"""
This module deals with object's attributes.

"""
def add_attribute(obj, att, value):
    """
    If possible, adds a new attribute to an object.

    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
