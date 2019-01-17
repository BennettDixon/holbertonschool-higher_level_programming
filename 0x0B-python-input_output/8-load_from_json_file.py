#!/usr/bin/python3
"""module for loading data from .json files
"""


import json


def load_from_json_file(filename):
    """loads an object from json file containing json string
        -> handles NO exceptions
    """
    with open(filename, encoding='utf-8') as myFile:
        return (json.loads(myFile.read()))
