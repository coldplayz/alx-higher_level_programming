#!/usr/bin/python3
'''Module for Rectangle class.
'''
from models.base import Base


class Rectangle(Base):
    '''A subclass of Base.
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Class constructor
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''Gets width
        '''
        return self.__width

    @width.setter
    def width(self, width):
        '''Sets width
        '''
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        '''Gets height
        '''
        return self.__height

    @height.setter
    def height(self, height):
        '''Sets height
        '''
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        '''Gets x
        '''
        return self.__x

    @x.setter
    def x(self, x):
        '''Sets x
        '''
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        '''Gets y
        '''
        return self.__y

    @y.setter
    def y(self, y):
        '''Sets y
        '''
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        '''Returns the area of the Rectangle instance
        '''
        return self.__width * self.__height

    def display(self):
        '''Displays the Rectangle with a # character.
        '''
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
        '''Updates the instance attribute
        '''
        attrs = ['id', 'width', 'height', 'x', 'y']

        if len(args):
            for attr_idx in range(len(args)):
                setattr(self, attrs[attr_idx], args[attr_idx])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        '''Returns a dictionary representing an instance.
        '''
        dct = dict(self.__dict__)
        dct2 = {}
        dct_cpy = dct.copy()
        for key in dct_cpy:
            if 'width' in key:
                dct2.update(width=dct[key])
                del dct[key]
            elif 'height' in key:
                dct2.update(height=dct[key])
                del dct[key]
            elif 'x' in key:
                dct2.update(x=dct[key])
                del dct[key]
            elif 'y' in key:
                dct2.update(y=dct[key])
                del dct[key]
        dct.update(dct2)
        return dct

    def __str__(self):
        '''String representation.
        '''
        return f"[{self.__class__.__name__}] ({self.id})" +\
            f" {self.__x}/{self.__y} - {self.__width}/{self.__height}"
