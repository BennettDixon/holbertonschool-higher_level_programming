#!/usr/bin/python3
"""module for use in testing
    base class
"""


import os
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
        """tests id being set when given and not upticking default
        """
        b = Base()
        b2 = Base(24)
        b3 = Base(45)
        b4 = Base()
        self.assertEqual(45, b3.id)
        self.assertEqual(b.id + 1, b4.id)

    def test_json_method(self):
        """tests Base's to_json_string method
        """
        r1 = Rectangle(4, 5, 6, 7, 8)
        r2 = Rectangle(10, 11, 12, 13, 14)
        dictionary = r1.to_dictionary()
        d2 = r2.to_dictionary()
        json_dict = Base.to_json_string([dictionary, d2])
        j_d = eval(json_dict)
        self.assertEqual(j_d[0]['id'], 8)
        self.assertEqual(j_d[1]['x'], 12)

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

    def test_from_json(self):
        """tests bases from_json_string method to convert string to
                -> list of dictionaries
        """
        s = Square(4, 8, 9, 2)
        r = Rectangle(9, 2, 3, 4)
        r_d = r.to_dictionary()
        s_d = s.to_dictionary()
        json_d = Base.to_json_string([s_d, r_d])
        d_list = Base.from_json_string(json_d)
        self.assertEqual(d_list[0]['id'], 2)
        self.assertEqual(d_list[1]['width'], 9)
        self.assertEqual(len(d_list), 2)

    def test_from_json_empty(self):
        """tests base's from_json_string method with empty inputs
        """
        d_list = Base.from_json_string("")
        self.assertEqual(len(d_list), 0)
        d_list = Base.from_json_string(None)
        self.assertEqual(len(d_list), 0)

    def test_create_inst(self):
        r = Rectangle(9, 2, 3, 4, 45)
        s = Square(4, 8, 9, 2)
        r_d = r.to_dictionary()
        s_d = s.to_dictionary()
        r2 = Rectangle.create(**r_d)
        s2 = Square.create(**s_d)
        self.assertEqual(s.id, s2.id)
        self.assertEqual(r.id, r2.id)
        self.assertEqual(s.y, s2.y)
        self.assertEqual(s.x, s2.x)
        self.assertEqual(r.width, r2.width)
        self.assertEqual(s.size, s2.size)

    def test_read_from_file(self):
        """tests the base class method read from file, for use in
            -> Rectangle and Square
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output[0].y, 8)
        self.assertEqual(list_rectangles_output[1].height, 4)

    def test_read_from_file_empty(self):
        try:
            os.remove('Square.json')
        except:
            pass
        list_output = Square.load_from_file()
        self.assertEqual(len(list_output), 0)
