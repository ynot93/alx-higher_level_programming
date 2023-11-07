#!/usr/bin/python3
"""
This module deals with data serialization.

"""
import json


def from_json_string(my_str):
    """
    Returns Python object represented by JSON string.

    """
    return json.loads(my_str)
