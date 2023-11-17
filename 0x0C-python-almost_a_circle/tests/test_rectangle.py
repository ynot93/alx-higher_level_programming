import unittest
from models.rectangle import Rectangle


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

    def test_rectangle_area(self):
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


if __name__ == "__main__":
    unittest.main()
