#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Delete keys with a specific value in dictionary"""
    keys = [key for key, val in a_dictionary.items() if val == value]

    for i in keys:
        del a_dictionary[i]

    return a_dictionary
