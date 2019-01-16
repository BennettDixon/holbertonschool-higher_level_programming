#!/usr/bin/python3


def is_same_class(obj, a_class):
    """checks if two objects are EXACTLY the same class
        -> doesn't care about inheritance
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class must be of type 'type'")
    return (type(obj) is a_class)
