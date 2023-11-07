#!/usr/bin/python3
"""
This module contains File I/O operations.

"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a lne of text into a file after a specifc string.

    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)

            if search_string in line:
                file.write(new_string + '\n')
