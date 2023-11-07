#!/usr/bin/python3
"""
This module handles file I/O operations.

"""


def append_write(filename="", text=""):
    """
    Append string at the end of a file and return number
    of characters added.

    """
    with open(filename, 'a', encoding='utf-8') as file:
        data = file.write(text)
    return data
