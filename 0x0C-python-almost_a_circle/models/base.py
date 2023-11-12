#!/usr/bin/python3
"""
This module deals with the Base class which will be imported
by all other classes in this project.

"""
import json


class Base:
    """
    This class manages id attribute in all future classes.

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes objects of this class with an integer id.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to JSON string representation.

        """
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes JSON string representation to a file.

        """
        if list_objs is None:
            list_objs = []

        file_name = "{}.json".format(cls.__name__)
        list_dicts = [item.to_dictionary() for item in list_objs]

        json_str = cls.to_json_string(list_dicts)

        with open(file_name, 'w') as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns list of the JSon string representation.

        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        """
        if cls.__name__ == "Square":
            inst = Square(5)
        elif cls.__name__ == "Rectangle":
            inst = Rectangle(3, 2)

        inst.update(**dictionary)

        return inst


