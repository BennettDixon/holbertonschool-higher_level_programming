#!/usr/bin/python3
"""module for use with square class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """square class for use as an object,
        -> inherits from rectangle,
        -> rectangle inherits from Base
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        builder = "[Square] ({}) {}/{} - {}".format(self.id,
                                                    self.x,
                                                    self.y,
                                                    self.width)
        return builder

    def update(self, *args, **kwargs):
        """takes an *args argument and sets arguments respective
            to instantiation function
        """
        if args != None and len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        elif kwargs is not None:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value


    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
