#!/usr/bin/python3
"""module for deserializing json data back to python objects
"""


import json


def from_json_string(my_str):
    """deserializes a JSON string back to a python object
        -> handles NO exceptions
    """
    return json.loads(my_str)
