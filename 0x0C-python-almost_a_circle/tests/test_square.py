import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_square_area(self):
        obj = Square(5)
        self.assertEqual(obj.area(), 25)

    def test_square_str_representation(self):
        obj = Square(6, 2, 1, 5)
        self.assertEqual(str(obj), "[Square] (5) 2/1 - 6")


if __name__ == "__main__":
    unittest.main()
