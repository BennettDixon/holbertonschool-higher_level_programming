#!/usr/bin/python3


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square shape class, super class is BaseGeometry, then Rectangle
    """
    def __init__(self, size):
        """instantiation method for class
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """overide magic str method for class
        """
        string = "[Square] " + str(self.__size) + '/'
        string += str(self.__size)
        return string
