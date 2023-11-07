#!/usr/bin/python3
"""
This module handles Python Input/Output operations.

"""

def read_file(filename=""):
    """
    Reads a text file(UTF8) and prints it to stdout.

    """
    with open(filename, 'r') as file:
        data = file.read()
        print(data)
