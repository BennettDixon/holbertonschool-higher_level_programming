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

