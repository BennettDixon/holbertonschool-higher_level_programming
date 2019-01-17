#!/usr/bin/python3


class Student:
    """student class for use
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dict rep of Student in json form
        """
        return {key: value for (key, value) in self.__dict__.items()
                if key in list(self.__dict__.keys())}
