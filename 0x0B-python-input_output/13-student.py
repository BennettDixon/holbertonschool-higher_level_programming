#!/usr/bin/python3


class Student:
    """student class for use
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dict rep of Student in json form
        """
        is_all_strs = True
        if isinstance(attrs, list):
            for ele in attrs:
                if not isinstance(ele, str):
                    is_all_strs = False
        else:
            is_all_strs = False

        return {key: value for (key, value) in self.__dict__.items()
                if key in list(self.__dict__.keys()) and
                (not is_all_strs or key in attrs)}

    def reload_from_json(self, json):
        """reloads an object from a json dictionary
            -> assumes json to always be a dictionary
        """
        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
