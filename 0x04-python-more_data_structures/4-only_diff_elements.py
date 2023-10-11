#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Returns set of elements present in only one set"""
    result = set_1 ^ set_2
    return result
