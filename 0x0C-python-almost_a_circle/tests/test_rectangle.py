import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_rectangle_area(self):
        obj = Rectangle(3, 4)
        self.assertEqual(obj.area(), 12)


if __name__ == "__main__":
    unittest.main()
