#!/usr/bin/python3
"""rectangle module for use
"""


from models.base import Base


class Rectangle(Base):
    """rectangle class for use
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """override for str method used in print etc
        """
        builder = "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                   self.id,
                                                   self.x,
                                                   self.y,
                                                   self.width,
                                                   self.height)
        return builder

    def area(self):
        """returns the area value of given rectangle instance
        """
        return (self.width * self.height)

    def display(self):
        """prints the rectangle to stdout
        """
        for y_sp in range(0, self.y):
            print()
        for i in range(0, self.height):
            builder = ""
            for x_sp in range(0, self.x):
                builder += " "
            for j in range(0, self.width):
                builder += "#"
            print(builder)

    def update(self, *args, **kwargs):
        """takes an *args argument and sets arguments respective
            to instantiation function
        """
        if args is not None and len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        elif kwargs is not None:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns dictionary representation of current rectangle
        """
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}

    def to_csv(self):
        """returns a list containing csv representation of rectangle
        """
        return [self.id, self.width, self.height, self.x, self.y]

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
