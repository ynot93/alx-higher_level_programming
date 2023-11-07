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

    def to_json(self):
        """
        Returns dict representation of a Student instance.

        """
        return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
        }
