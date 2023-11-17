import unittest
from models.rectangle import Rectangle
import os


class TestRectangle(unittest.TestCase):
    def test_create_instance_exists(self):
        obj = Rectangle(1, 2)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)


    def test_create_instance_with_x(self):
        obj = Rectangle(1, 2, 3)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 3)

    def test_create_instance_with_x_and_y(self):
        obj = Rectangle(1, 2, 3, 4)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

    def test_create_instance_with_invalid_width(self):
        with self.assertRaises(TypeError) as e:
            obj = Rectangle("1", 2)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_create_instance_with_invalid_height(self):
        with self.assertRaises(TypeError) as e:
            obj = Rectangle(1, "2")
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_create_instance_with_invalid_x(self):
        with self.assertRaises(TypeError) as e:
            obj = Rectangle(1, 2, "3")
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_create_instance_with_invalid_y(self):
        try:
            obj = Rectangle(1, 2, 3, "4")
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_create_instance_with_excess_arguments(self):
        with self.assertRaises(TypeError) as e:
            obj = Rectangle(1, 2, 3, 4, 5, 6)
        self.assertEqual(str(e.exception), "Unexpected positional arguments")

    def test_instance_with_negative_width(self):
        with self.assertRaises(ValueError) as e:
            obj = Rectangle(-1, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_instance_with_negative_height(self):
        with self.assertRaises(ValueError) as e:
            obj = Rectangle(1, -2)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_instance_with_zero_width(self):
        with self.assertRaises(ValueError) as e:
            obj = Rectangle(0, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_instance_with_zero_height(self):
        with self.assertRaises(ValueError) as e:
            obj = Rectangle(1, 0)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_instance_with_negative_x(self):
        with self.assertRaises(ValueError) as e:
            obj = Rectangle(1, 2, -3)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_instance_with_negative_y(self):
        with self.assertRaises(ValueError) as e:
            obj = Rectangle(1, 2, 3, -4)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_objangle_area(self):
        obj = Rectangle(3, 4)
        self.assertEqual(obj.area(), 12)

    def test_str_method(self):
        obj = Rectangle(1, 2, 3, 4, 7)
        self.assertEqual(str(obj), "[Rectangle] (7) 3/4 - 1/2")

    def test_display_without_x_and_y(self):
        obj = Rectangle(1, 2)
        obj.display()

    def test_display_without_y(self):
        obj = Rectangle(1, 2, 3)
        obj.display()

    def test_display_method(self):
        obj = Rectangle(1, 2, 3, 4)
        obj.display()

    def test_to_dictionary(self):
        obj = Rectangle(5, 6, 7, 8, 9)
        self.assertEqual(obj.to_dictionary(), {'id': 9, 'width': 5, 'height': 6, 'x': 7, 'y': 8})

    def test_update_method(self):
        obj = Rectangle(2, 3, 4, 5)
        obj.update(6, 7, 8, 9, 10)
        self.assertEqual(str(obj), "[Rectangle] (6) 9/10 - 7/8")

    def test_update_method_with_dict(self):
        obj = Rectangle(2, 3, 4, 5)
        obj.update(**{'id': 89})
        self.assertEqual(str(obj), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_method_with_dict_and_width(self):
        obj = Rectangle(2, 3, 4, 5)
        obj.update(**{'id': 89, 'width': 1})
        self.assertEqual(str(obj), "[Rectangle] (89) 4/5 - 1/3")

    def test_update_method_with_dict_and_width_height(self):
        obj = Rectangle(2, 3, 4, 5)
        obj.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(str(obj), "[Rectangle] (89) 4/5 - 1/2")

    def test_update_method_with_dict_and_all_attributes(self):
        obj = Rectangle(2, 3, 4, 5)
        obj.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(str(obj), "[Rectangle] (89) 3/4 - 1/2")

    def test_create_method_with_dict(self):
        obj = Rectangle.create(**{'id': 89})
        self.assertEqual(obj.id, 89)

    def test_create_method_with_dict_and_width(self):
        obj = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(obj.width, 1)

    def test_create_method_with_dict_and_width_height(self):
        obj = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(obj.height, 2)

    def test_create_method_with_dict_and_all_attributes(self):
        obj = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

    def test_save_to_file_method_with_None(self):
        Rectangle.save_to_file(None)

    def test_save_to_file_method_with_empty_list(self):
        Rectangle.save_to_file([])

    def test_save_to_file_method_with_list_of_objangles(self):
        Rectangle.save_to_file([Rectangle(1, 2)])

    def test_load_from_file_method_when_file_doesnt_exist(self):
        objs = Rectangle.load_from_file()
        try:
            os.remove("Rectangle.json")
        except:
            pass
        self.assertEqual(objs, [])

    def test_load_from_file_method_when_file_exists(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        objs = Rectangle.load_from_file()
        self.assertEqual(len(objs), 1)


if __name__ == "__main__":
    unittest.main()
