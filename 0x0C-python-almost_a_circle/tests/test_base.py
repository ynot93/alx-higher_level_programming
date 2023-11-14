#!/usr/bin/python3

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Setting up initial variables for the tests."""
        Base._Base__nb_objects = 0
        cls.rectangle1 = Rectangle(1, 2, 3, 4, 5)
        cls.rectangle2 = Rectangle(10, 20, 30, 40, 50)
        cls.square1 = Square(1, 2, 3, 4)
        cls.square2 = Square(10, 20, 30, 40)
        cls.rectangles = [cls.rectangle1, cls.rectangle2]
        cls.squares = [cls.square1, cls.square2]

    @classmethod
    def tearDownClass(cls):
        """Cleaning up after the tests."""
        del cls.rectangle1
        del cls.rectangle2
        del cls.square1
        del cls.square2

    def test_base_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
    
    def test_empty_list(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_non_empty_list(self):
        data = [{'id': 1, 'name': 'Item 1'}, {'id': 2, 'name': 'Item 2'}]
        json_str = Base.to_json_string(data)
        self.assertEqual(json_str, '[{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]')

    def test_empty_json(self):
        data = Base.from_json_string("[]")
        self.assertEqual(data, [])

    def test_non_empty_json(self):
        json_str = '[{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]'
        data = Base.from_json_string(json_str)
        self.assertEqual(data, [{'id': 1, 'name': 'Item 1'}, {'id': 2, 'name': 'Item 2'}])


    def test_save_to_file(self):
        Base.save_to_file(self.rectangles)
        with open("Rectangle.json", "r") as file:
            json_str = file.read()
            self.assertTrue(len(json_str) > 0)

        Base.save_to_file(self.squares)
        with open("Square.json", "r") as file:
            json_str = file.read()
            self.assertTrue(len(json_str) > 0)

    def test_load_from_file(self):
        rectangles = Base.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertEqual(rectangles[0].id, 5)
        self.assertEqual(rectangles[0].width, 1)
        self.assertEqual(rectangles[0].height, 2)
        self.assertEqual(rectangles[0].x, 3)
        self.assertEqual(rectangles[0].y, 4)

        squares = Base.load_from_file()
        self.assertEqual(len(squares), 2)
        self.assertIsInstance(squares[0], Square)
        self.assertEqual(squares[0].id, 4)
        self.assertEqual(squares[0].size, 1)
        self.assertEqual(squares[0].x, 2)
        self.assertEqual(squares[0].y, 3)

    def test_save_to_file_empty(self):
        Base.save_to_file(None)
        for filename in ["Rectangle.json", "Square.json"]:
            self.assertFalse(os.path.exists(filename))

    def test_load_from_file_empty(self):
        os.remove("Rectangle.json")
        os.remove("Square.json")
        rectangles = Base.load_from_file()
        squares = Base.load_from_file()
        self.assertEqual(rectangles, [])
        self.assertEqual(squares, [])
if __name__== "__main__":
    unittest.main()
