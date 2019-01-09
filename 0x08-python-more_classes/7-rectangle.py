#!/usr/bin/python3


class Rectangle():
    """rectangle class for storing rectangle data
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ instantiation method for object creation
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ provides __str__ method for object when str()
            or print() is called
        """
        if self.width == 0 or self.height == 0:
            return ""

        string = ""
        for i in range(0, self.height):
            for j in range(0, self.width):
                string += str(self.print_symbol)
            if i != self.height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """ provides __repr__ method for object when repr()
            is called, or eval().
        """
        string = "Rectangle("
        string += str(self.width)
        string += ", " + str(self.height) + ")"
        return string

    def __del__(self):
        """ called when a rectangle instance is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def height(self):
        """ getter for height property """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height property """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """ getter for width property """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width property """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """ gets the area of rectangle instance """
        return (self.width * self.height)

    def perimeter(self):
        """ gets the perimeter of a rectangle instance """
        if self.width == 0 or self.height == 0:
            return 0
        return ((2 * self.width) + (2 * self.height))
