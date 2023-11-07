#!/usr/bin/python3
"""
This module deals with JSON (de)serialization.

"""


def class_to_json(obj):
    """
    Converts an object into a dict representation for JSON
    serialization of an object.

    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("Object is not serializable")

    obj_dict = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, str, dict, int, bool)):
            obj_dict[key] = value

    return obj_dict
