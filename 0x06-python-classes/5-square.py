#!/usr/bin/python3
'''Module for the square class'''


class Square:
    '''Creates a square class'''

    def __init__(self, size=0):
        self.size = size  # automatically checked by property

    def area(self):
        '''returns square area'''
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        '''sets the size attribute'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        '''prints # based on square of size'''
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
        elif self.__size == 0:
            print()
