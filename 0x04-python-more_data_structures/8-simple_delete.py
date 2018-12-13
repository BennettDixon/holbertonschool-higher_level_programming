#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """
    deletes an element based on the key from a dictionary
    """
    if key is not "" and key in a_dictionary:
        a_dictionary.pop(key)
    return (a_dictionary.copy())
