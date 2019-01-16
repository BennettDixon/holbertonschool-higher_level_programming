#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """checks if an object is sort of a class
        -> through inheritance
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class type must be 'type'")
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
