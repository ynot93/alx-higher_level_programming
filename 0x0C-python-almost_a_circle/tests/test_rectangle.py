import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_rectangle_area(self):
        obj = Rectangle(3, 4)
        self.assertEqual(obj.area(), 12)

    def test_rectangle_str_representation(self):
        obj = Rectangle(5, 5)
        self.assertEqual(str(obj), "[Rectangle] (2) 0/0 - 5/5")


if __name__ == "__main__":
    unittest.main()
