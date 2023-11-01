#!/usr/bin/python3
"""

This is a module that adds the value of two numbers that are first
typecast to integers before the operation is performed.

"""


def add_integer(a, b=98):
    """
    Takes arguments 'a' and 'b' which must be integers or floats and
    adds them together.

    Args:
        a (int or float): First argument.
        b (int or float): Second argument. (defaults to 98)

    Returns:
        int: The sum of 'a' and 'b'.

    Raises:
        TypeError: If 'a' or 'b' are neither int nor float.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
