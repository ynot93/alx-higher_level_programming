#!/usr/bin/python3
def no_c(my_string):
    """Remove all characters c and C from a string."""
    string = ""
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            string += letter
    return string
