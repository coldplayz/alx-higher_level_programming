#!/usr/bin/python3
'''
Class Rectangle.
'''


class Rectangle:
    '''Defines a rectangle.
    '''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0

        return (2 * self.height) + (2 * self.width)

    def __str__(self):
        strr = ""

        if self.width == 0 or self.height == 0:
            return strr

        for row in range(self.height):
            for col in range(self.width):
                strr += '#'
            strr += "" if row == self.height - 1 else "\n"

        return strr

    def __repr__(self):
        return f"{self.__class__.__name__}({self.width}, {self.height})"
