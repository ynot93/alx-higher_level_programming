import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_base_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)


if __name__== "__main__":
    unittest.main()
