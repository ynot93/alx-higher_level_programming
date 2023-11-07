#!/usr/bin/python3
"""
This module contains class MyInt

"""


class MyInt(int):
    """
    Invert int operations == and !=

    """
    def __eq__(self, value):
        """
        Invert == operation

        """
        return self.real != value

    def __ne__(self, value):
        """
        Invert != operation

        """
        return self.real == value
