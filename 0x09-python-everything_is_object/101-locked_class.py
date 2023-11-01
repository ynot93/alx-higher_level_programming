#!/usr/bin/python3
"""
Defines class  with no class or object attribute.

"""
class LockedClass:
    """
    Prevents the user from creating new instance attributes
    except if the new instnce attribute is called "first_name"

    """
    __slots__ = ["first_name"]
