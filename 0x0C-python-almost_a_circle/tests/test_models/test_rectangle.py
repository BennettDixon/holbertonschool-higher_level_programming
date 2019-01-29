#!/usr/bin/python3
"""module for use in testing
    rectangle class
"""


import sys
import unittest
from models.rectangle import Rectangle
from capture_manager import capture


class TestRectangle(unittest.TestCase):
    """class for test case for rectangle class
    """

    def test_basic_id(self):
        """tests basic functionality
        """
        b = Rectangle(10, 2)
        b2 = Rectangle(2, 10)
        b3 = Rectangle(3, 10)
        self.assertEqual(b2.id + 1, b3.id)

    def test_given_id(self):
        b = Rectangle(10, 2)
        b2 = Rectangle(10, 3)
        b3 = Rectangle(10, 4)
        b4 = Rectangle(10, 5, 0, 0, 42)
        self.assertEqual(b2.id + 1, b3.id)
        self.assertEqual(42, b4.id)

    def test_input_types(self):
        with self.assertRaises(TypeError):
            n = Rectangle("hello", "world")
        with self.assertRaises(TypeError):
            n = Rectangle(5.4, 3.8)
        with self.assertRaises(TypeError):
            n = Rectangle(4, 8, "hello", "world")
        with self.assertRaises(TypeError):
            n = Rectangle(4, 8, 5.12, 5.9)
        with self.assertRaises(TypeError):
            n = Rectangle(True, False, True, False)

    def test_input_values(self):
        with self.assertRaises(ValueError):
            n = Rectangle(0, 0)
        with self.assertRaises(ValueError):
            n = Rectangle(1, 1, -5, -2)

    def test_area(self):
        r = Rectangle(4, 8)
        self.assertEqual(r.area(), 32)

    def test_str(self):
        r = Rectangle(3, 3, 2, 2, 14)
        self.assertEqual("[Rectangle] (14) 2/2 - 3/3", str(r))
        r = Rectangle(5, 5, 1)
        self.assertEqual("[Rectangle] ({}) 1/0 - 5/5".format(r.id), str(r))

    def test_update(self):
        r = Rectangle(4, 5, 45)
        r.update(500)
        self.assertEqual(500, r.id)
        r.update(500, 2)
        self.assertEqual(2, r.width)
        r.update(500, 2, 3)
        self.assertEqual(3, r.height)
        r.update(500, 2, 3, 4)
        self.assertEqual(4, r.x)
        r.update(500, 2, 3, 4, 5)
        self.assertEqual(5, r.y)
        r.update(500, 2, 3, 4, 5, 6, 7, 8)
        self.assertEqual(5, r.y)

    def test_kwarg_update(self):
        r = Rectangle(4, 5, 0, 0, 33)
        r.update(45, id=32, width=42)
        self.assertEqual(45, r.id)
        r.update(45, 10, 10, x=5, y=6)
        self.assertEqual(0, r.x)
        self.assertEqual(10, r.width)
        self.assertEqual(45, r.id)
        r.update(width=4)
        self.assertEqual(4, r.width)
        r.update(width=6, id=6, height=45)
        self.assertEqual(6, r.width)
        self.assertEqual(6, r.id)
        self.assertEqual(45, r.height)
        r.update(x=100, y=100)
        self.assertEqual(6, r.id)
        self.assertEqual(100, r.x)
        self.assertEqual(100, r.y)

    def test_dictionary(self):
        """tests rectangle's to_dictionary method
        """
        r = Rectangle(4, 5, 6, 7, 33)
        r_dict = r.to_dictionary()
        self.assertEqual(r_dict['id'], 33)
        self.assertEqual(r_dict['width'], 4)
        self.assertEqual(r_dict['height'], 5)
        self.assertEqual(r_dict['x'], 6)
        self.assertEqual(r_dict['y'], 7)
