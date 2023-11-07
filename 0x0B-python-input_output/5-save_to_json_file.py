#!/usr/bin/python3
"""
This module deals with JSON (de)serialization.

"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes object to test file using JSON representation.

    """
    with open(filename, 'w') as file:
        data = file.write(json.dumps(my_obj))
