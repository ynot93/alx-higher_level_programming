import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_obj_with_positive_size(self):
        obj = Square(1)
        self.assertEqual(str(obj), "[Square] (39) 0/0 - 1")

    def test_obj_with_positive_size_and_position(self):
        obj = Square(1, 2)
        self.assertEqual(str(obj), "[Square] (41) 2/0 - 1")

    def test_obj_with_positive_size_position_and_id(self):
        obj = Square(1, 2, 3)
        self.assertEqual(str(obj), "[Square] (43) 2/3 - 1")

    def test_obj_with_string_size(self):
        with self.assertRaises(TypeError) as e:
            obj = Square("1")
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_obj_with_positive_size_and_string_position(self):
        with self.assertRaises(TypeError) as e:
            obj = Square(1, "2")
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_obj_with_positive_size_position_and_string_id(self):
        with self.assertRaises(TypeError) as e:
            obj = Square(1, 2, "3")
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_obj_with_negative_size(self):
        with self.assertRaises(ValueError) as e:
            obj = Square(-1)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_obj_with_positive_size_and_negative_position(self):
        with self.assertRaises(ValueError) as e:
            obj = Square(1, -2)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_obj_with_positive_size_position_and_negative_id(self):
        with self.assertRaises(ValueError) as e:
            obj = Square(1, 2, -3)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_obj_with_zero_size(self):
        with self.assertRaises(ValueError) as e:
            obj = Square(0)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_str_method_for_obj(self):
        obj = Square(1, 2, 3)
        self.assertEqual(str(obj), "[Square] (49) 2/3 - 1")

    def test_to_dictionary_method_for_obj(self):
        obj = Square(1, 2, 3)
        expected_dict = {'id': 50, 'size': 1, 'x': 2, 'y': 3}
        self.assertEqual(obj.to_dictionary(), expected_dict)

    def test_update_method_for_obj(self):
        obj = Square(1, 2, 3)
        obj.update(89)
        self.assertEqual(str(obj), "[Square] (89) 2/3 - 1")

    def test_update_method_with_id_for_obj(self):
        obj = Square(1, 2, 3)
        obj.update(89, 5)
        self.assertEqual(str(obj), "[Square] (89) 2/3 - 5")

    def test_update_method_with_id_and_size_for_obj(self):
        obj = Square(1, 2, 3)
        obj.update(89, 1, 3)
        self.assertEqual(str(obj), "[Square] (89) 3/3 - 1")

    def test_update_method_with_id_size_and_position_for_obj(self):
        obj = Square(5, 4, 3)
        obj.update(89, 2, 2, 3)
        self.assertEqual(str(obj), "[Square] (89) 2/3 - 2")

    def test_update_method_with_dict_for_obj(self):
        obj = Square(1, 2, 3)
        obj.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(obj), "[Square] (89) 2/3 - 1")

    def test_create_method_with_dict_for_obj(self):
        obj = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(obj), "[Square] (89) 2/3 - 1")

    def test_save_to_file_method_with_None_for_obj(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_method_with_empty_list_for_obj(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_method_with_list_of_objs_for_obj(self):
        obj = Square(1, 2, 3)
        Square.save_to_file([obj])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 48, "size": 1, "x": 2, "y": 3}]')

    def test_load_from_file_method_when_file_doesnt_exist_for_obj(self):
        objs = Square.load_from_file()
        self.assertEqual(objs, [])

    def test_load_from_file_method_when_file_for_obj(self):
        obj = Square(1, 2, 3)
        Square.save_to_file([obj])
        objs = Square.load_from_file()
        self.assertEqual(str(objs[0]), "[Square] (36) 2/3 - 1")


if __name__ == "__main__":
    unittest.main()
