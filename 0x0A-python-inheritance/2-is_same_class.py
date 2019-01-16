#!/usr/bin/python3


def is_same_class(obj, a_class):
    """checks if two objects are EXACTLY the same class
        -> doesn't care about inheritance
    """
    return (type(obj) is a_class)
