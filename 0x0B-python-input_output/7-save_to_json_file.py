#!/usr/bin/python3
"""module for use in writing json strings to files
"""


import json


def save_to_json_file(my_obj, filename):
    """saves obj to a file, overwriting previous contents
        -> handles NO exceptions
        -> encoded as utf-8
       Return: number of bytes written to file.
    """
    with open(filename, 'w', encoding='utf-8') as myFile:
        return myFile.write(json.dumps(my_obj))
