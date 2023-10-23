#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer with string format"""
    try:
        print("{:d}".format(int(value)))
        return True
    except (TypeError, ValueError):
        return False
