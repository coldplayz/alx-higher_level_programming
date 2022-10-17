#!/usr/bin/python3
'''
Class Rectangle.
'''


class Rectangle:
    '''Defines a rectangle.
    '''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Compares rect_1 and rect_2 for size.

        Args:
            rect_1 (Rectangle): a Rectangle object.
            rect_2 (Rectangle): a Rectangle object.

        Returns:
            Rectangle: the biggest Rectangle by area.

        Raises:
            TypeError: if arguments are not instances of Rectangle.
        '''

        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        area1 = rect_1.area()
        area2 = rect_2.area()

        return rect_1 if area1 >= area2 else rect_2

    @classmethod
    def square(cls, size=0):
        '''Returns a new Rectangle instance.

        Args:
            size (int): length of all sides of the Rectangle.

        Returns:
            Rectangle: a new Rectangle with equal sides.

        Raises:
            TypeError: if size is not an integer, or is less than zero.
        '''

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        return cls(size, size)

    def __str__(self):
        strr = ""

        if self.width == 0 or self.height == 0:
            return strr

        for row in range(self.height):
            for col in range(self.width):
                strr += str(self.print_symbol)
            strr += "" if row == self.height - 1 else "\n"

        return strr

    def __repr__(self):
        return f"{self.__class__.__name__}({self.width}, {self.height})"

    def __del__(self):
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")
