#!/usr/bin/python3


class LockedClass:
    """Locked class: can't set instance attributes to it
    """
    def __setattr__(self, name, value):
        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '" + name + "'")
