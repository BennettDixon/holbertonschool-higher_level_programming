#!/usr/bin/python3
"""unit testing module for 6-max_integer_test.py
"""
import unittest
max_int = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    class for testing 6-max_integer_test.py
    """

    def test_max_integer(self):
        """ test case for normal list of integers w/o negatives
        """
        test_list = [1, 2, 3, 8, 4]
        self.assertEqual(max_int(test_list), 8)

    def test_max_integer_neg(self):
        """ test case for normal list of integers w/ negatives
        """
        test_list = [1, 2, 3, 8, 4, -40, -400, -12, 0]
        self.assertEqual(max_int(test_list), 8)

    def test_max_integer_(self):
        """ test case for empty list
        """
        self.assertEqual(max_int([]), None)
