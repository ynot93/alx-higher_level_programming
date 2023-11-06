#!/usr/bin/python3
"""
This module pracices inheritance through printing lists.

"""


class MyList(list):
    """
    This is a subclass that inherits from the superclass list.

    """
    def print_sorted(self):
        """
        prints the list sorted in ascending order.

        """
        my_list = sorted(self)
        print(my_list)
