#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """
    updates a dictionary and returns a new copy
    original is affected
    """
    a_dictionary.update({key: value})
    return (a_dictionary.copy())
