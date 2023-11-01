#!/usr/bin/python3
"""
This module prints the full names of a person.

"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>

    Args:
        first_name (string): Person's first name.
        last_name(last_name): Person's last name (defaults to empty).

    Returns:
        string: Containing the person's full name.

    Raises:
        TypeError: if first or last names are not strings.

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
