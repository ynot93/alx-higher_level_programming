#!/usr/bin/python3
"""
This module deals with the Base class which will be imported
by all other classes in this project.

"""
import json
import csv
import turtle


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
        Returns list of the JSON string representation.

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
            inst = cls(5)
        elif cls.__name__ == "Rectangle":
            inst = cls(3, 2)

        inst.update(**dictionary)

        return inst

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a JSON file.

        """
        file_name = "{}.json".format(cls.__name__)

        try:
            with open(file_name, 'r') as file:
                json_str = file.read()
                list_data = json.loads(json_str)
                return [cls.create(**attr) for attr in list_data]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes in CSV Format.

        """
        file_name = "{}.csv".format(cls.__name__)
        with open(file_name, mode='w', newline='') as file:
            written = csv.writer(file)
            for item in list_objs:
                if cls.__name__ == "Rectangle":
                    written.writerow([item.id, item.width, item.height, item.x, item.y])
                if cls.__name__ == "Square":
                    written.writerow([item.id, item.size, item.x, item.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes in CSV Format.

        """
        file_name = "{}.csv".format(cls.__name__)
        list_objs = []

        try:
            with open(file_name, mode='r') as file:
                read = csv.reader(file)
                for row in read:
                    if cls.__name__ == "Rectangle":
                        obj = cls(int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        obj = cls(int(row[1]), int(row[2]), int(row[3]), int(row[0]))
                    list_objs.append(obj)
            return list_objs
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles and Squares.

        """
        window = turtle.Screen()
        window.title("These are the drawn rectangles or squares")
        t = turtle.Turtle()
        t.speed(1)

        for rectangle in list_rectangles:
            t.penup()
            t.goto(rectangle.x, rectangle.y)
            t.pendown()
            t.color("yellow")
            t.begin_fill()
            for _ in range(2):
                t.forward(rectangle.width)
                t.left(90)
                t.forward(rectangle.height)
                t.left(90)
            t.end_fill()

        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            t.color("blue")
            t.begin_fill()
            for _ in range(4):
                t.forward(square.size)
                t.left(90)
            t.end_fill()

        turtle.done()
