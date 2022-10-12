#!/usr/bin/python3
'''Module for the square class'''


class Square:
    '''Creates a square class'''

    def __init__(self, size=0, position=(0, 0)):
        self.size = size  # automatically checked by property
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or\
                len(value) != 2 or type(value[0]) is not int or\
                value[0] < 0 or type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        '''prints # based on square of size'''
        if self.__size > 0:
            for i in range(self.__size):
                if i == 0:
                    for k in range(self.__position[1]):
                        print()
                for j in range(self.__size):
                    if j == 0:
                        for m in range(self.__position[0]):
                            print(end=" ")
                    print('#', end='')
                print()
        elif self.__size == 0:
            print()

    def __str__(self):
        strr = ""
        if self.__size > 0:
            for i in range(self.__size):
                if i == 0:
                    for k in range(self.__position[1]):
                        strr += "\n"
                for j in range(self.__size):
                    if j == 0:
                        for m in range(self.__position[0]):
                            strr += " "
                    strr += "#"
                strr += "" if i == (self.__size - 1) else "\n"
        elif self.__size == 0:
            strr = ""
        return strr
