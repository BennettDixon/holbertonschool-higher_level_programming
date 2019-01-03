#!/usr/bin/python3


class Square:
    """
    class square that has attributes:
        size
    some attributes are protected from input.
    """
    def __init__(self, size=0):
        """
        initialization function for our square clasee
        """
        if self.__validate_size(size):
            self.__size = size

    def __eq__(self, other):
        """
        used by == to check equality
        """
        return (self.area() == other.area())

    def __ne__(self, other):
        """
        used by != to check equality
        """
        return (self.area() != other.area())

    def __lt__(self, other):
        """
        used by < to check equality
        """
        return (self.area() < other.area())

    def __le__(self, other):
        """
        used by <= to check equality
        """
        return (self.area() <= other.area())

    def __gt__(self, other):
        """
        used by > to check equality
        """
        return (self.area() > other.area())

    def __ge__(self, other):
        """
        used by >= to check equality
        """
        return (self.area() >= other.area())

    @property
    def size(self):
        """
        getter for size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter for size attribute
        """
        if self.__validate_size(value):
            self.__size = value

    def area(self):
        """
        calculates the area of the square
        """
        return self.__size ** 2

    def __validate_size(self, size):
        """
        validates the size, checking for errors
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            return True
        return False
