#!/usr/bin/python3
"""module for use in testing
    base class
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """class for test case for base class
    """

    def test_basic(self):
        """tests basic functionality
        """
        b = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b2.id + 1, b3.id)

    def test_given_id(self):
        b = Base()
        b2 = Base(24)
        b3 = Base(45)
        b4 = Base()
        self.assertEqual(45, b3.id)
        self.assertEqual(b.id + 1, b4.id)
