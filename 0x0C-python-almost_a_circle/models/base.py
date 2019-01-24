#!/usr/bin/python3
"""module for use as base class
"""


class Base:
    """base class for use with other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiates the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns JSON string representation of list_dictionaries
        """
        return str(list_dictionaries)
