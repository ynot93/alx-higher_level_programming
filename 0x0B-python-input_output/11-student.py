#!/usr/bin/python3
"""
This module deals with JSON (de)serialization.

"""


class Student:
    """
    Defines a student.

    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize student with name and age attributes.

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dict representation of a Student instance.

        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        else:
            filtered_dict = {}
            for item in attrs:
                if hasattr(self, item):
                    filtered_dict[item] = getattr(self, item)
            return filtered_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        """
        for key, value in json.items():
            setattr(self, key, value)
