#!/usr/bin/python3
"""
This module deals with Python data serialization.

"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of a string.

    """
    return json.dumps(my_obj)
