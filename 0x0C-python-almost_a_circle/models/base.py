#!/usr/bin/python3
'''Module for class Base.
'''


class Base:
    '''The base class of the project.
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        if type(id) is not int and id is not None:
            raise TypeError("id must be an integer")
        if id is not None:
            self.id = id
            print("manual id", self.id)
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
            print("auto id", self.__class__.__nb_objects)
