#!/usr/bin/python3

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_base_id(self):
        obj1 = Base()
        self.assertEqual(obj1.id, 1)

    def test_base_id_plusone(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj2.id, 3)

    def test_custom_id(self):
        obj1 = Base(98)
        self.assertEqual(obj1.id, 98)

    def test_json_string_none(self):
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_empty_list(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_non_empty_list(self):
        data = [{'id': 1, 'name': 'Item 1'}, {'id': 2, 'name': 'Item 2'}]
        json_str = Base.to_json_string(data)
        self.assertEqual(json_str, '[{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]')

    def test_from_json_string_none(self):
        obj_json = Base.from_json_string(None)
        self.assertEqual(obj_json, [])

    def test_from_json_string_empty_list(self):
        obj_json = Base.from_json_string('[]')
        self.assertEqual(obj_json, [])

    def test_from_json_string_data(self):
        data = '[{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]'
        obj_json = Base.from_json_string(data)
        self.assertEqual(obj_json, [{'id': 1, 'name': 'Item 1'}, {'id': 2, 'name': 'Item 2'}])


if __name__ == "__main__":
    unittest.main()
