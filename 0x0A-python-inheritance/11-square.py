#!/usr/bin/python3
'''BaseGeometry class Module.
'''


class BaseGeometry:
    '''The BaseGeometry class.
    '''

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise TypeError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    '''A subclass of BaseGeometry.
    '''

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    '''A subclass of Rectangle.
    '''

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
