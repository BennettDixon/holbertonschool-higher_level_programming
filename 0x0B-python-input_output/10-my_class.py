#!/usr/bin/python3
""" My class module
"""

class MyClass:
    """ My class
    """

    def __init__(self, name):
        self.name = name
        self.number = 0
        self.lists = ["hi", "there", 4, "list"]
        self.listoflists = [[-1, 0], [1, 2]]
    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)
