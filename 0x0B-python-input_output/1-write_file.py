#!/usr/bin/python3
"""
This module deals with file I/O operations.

"""


def write_file(filename="", text=""):
    """
    Writes string to a txt file and return number of
    characters written.

    """
    with open(filename, 'w', encoding='utf-8') as file:
        data = file.write(text)
    return data
