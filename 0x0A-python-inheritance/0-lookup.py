#!/usr/bin/python3
"""
This module returns available attributes/methods of an object.

"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    """
    return list(dir(obj))
