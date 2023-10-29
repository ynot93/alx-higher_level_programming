#!/usr/bin/python3
"""
This module creates unit tests for the max_integer function.

"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    This class handles edgecases for max_integer function

    """
    def test_list_empty(self):
        self.assertIsNone(max_integer([]), "If list is empty, return None")

    def test_max(self):
        self.assertEqual(max_integer([2, 4, 9, 5]), 9, "Max integer found in list")

    def test_max_beginning(self):
        self.assertEqual(max_integer([9, 2, 4, 5]), 9, "Max integer found at beginning of list")

    def test_max_end(self):
        self.assertEqual(max_integer([2, 4, 5, 9]), 9, "Max integer found at end of list")

    def test_wrong_data_type(self):
        with self.assertRaises(TypeError):
            max_integer([9, 2, 4, "five"])

    def test_negative_data(self):
        self.assertEqual(max_integer([-9, -2, -4, -5]), -2, "Max of negative integers")

    def test_single_integer(self):
        self.assertEqual(max_integer([9]), 9, "Max of single integer")

    def test_multiple_max_integers(self):
        self.assertEqual(max_integer([2, 9, 4, 5, 9]), 9, "Max of multiple max integers")

if __name__ == "__main__":
    unittest.main()
