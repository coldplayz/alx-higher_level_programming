#!/usr/bin/python3
'''Module for Rectangle class.
'''
from models.base import Base


class Rectangle(Base):
    '''A subclass of Base.
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        return self.__width * self.__height

    def display(self):
        for row_idx in range(self.__height):
            if row_idx == 0:
                for newline in range(self.__y):
                    print()
            for col_idx in range(self.__width):
                if col_idx == 0:
                    for space in range(self.__x):
                        print(" ", end='')
                print("#", end='')
            print()

    def update(self, *args, **kwargs):
        attrs = ['id', 'width', 'height', 'x', 'y']

        if len(args):
            for attr_idx in range(len(args)):
                setattr(self, attrs[attr_idx], args[attr_idx])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        return dict(self.__dict__)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id})" +\
                f" {self.__x}/{self.__y} {self.__width}/{self.__height}"
