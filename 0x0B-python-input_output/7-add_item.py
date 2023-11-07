#!/usr/bin/python3
"""
This module deals with JSON serialization.

"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """
    Add all arguments to a Python list and save them to a file.

    """
    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []

    my_list.extend(sys.argv[1:])

    save_to_json_file(my_list, "add_item.json")


if __name__ == "__main__":
    main()
