#!/usr/bin/python3
"""module for use in testing
    base class
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_write_file_basic(self):
        """tests write to file basic capabilities, given 1 type of class
        """
        s = Square(3, 1, 1, 10)
        s2 = Square(4, 2, 2, 20)
        r1 = Rectangle(5, 6, 3, 3, 30)
        r2 = Rectangle(7, 8, 4, 4, 40)
        Base.save_to_file([s, s2])
        with open('Square.json', 'r', encoding='utf-8') as myFile:
            text = myFile.read()
        list_of_dicts = eval(text)
        self.assertEqual(list_of_dicts[0]['id'], 10)
        self.assertEqual(list_of_dicts[1]['x'], 2)

        Base.save_to_file([r1, r2])
        with open('Rectangle.json', 'r', encoding='utf-8') as myFile:
            text = myFile.read()
        list_of_dicts = eval(text)
        self.assertEqual(list_of_dicts[0]['id'], 30)
        self.assertEqual(list_of_dicts[1]['x'], 4)

    def test_write_file_complex(self):
        """tests writing a file with harder inputs
        """
        s = Square(3, 1, 1, 10)
        s2 = Square(4, 2, 2, 20)
        r1 = Rectangle(5, 6, 3, 3, 30)
        r2 = Rectangle(7, 8, 4, 4, 40)
        Base.save_to_file(["hello", 42, "more garb", True, s, s2])
        with open('Square.json', 'r', encoding='utf-8') as myFile:
            text = myFile.read()
        list_of_dicts = eval(text)
        self.assertEqual(list_of_dicts[0]['id'], 10)
        self.assertEqual(list_of_dicts[1]['x'], 2)

        Base.save_to_file([s, 89, r1, "garb", 42, s2, r2])
        with open('Rectangle.json', 'r', encoding='utf-8') as myFile:
            text = myFile.read()
        list_of_dicts = eval(text)
        self.assertEqual(list_of_dicts[1]['id'], 30)
        self.assertEqual(list_of_dicts[3]['x'], 4)
      

    def test_write_file_empty(self):
        """tests empty list is written to correct default file
        """
        Base.save_to_file([])
        with open('Rectangle.json', 'r', encoding='utf-8') as myFile:
            text = myFile.read()
        self.assertEqual(text, "[]")  
