#!/usr/bin/python3
'''Module for class Student.
'''


class Student:
    '''Defines the type Students.
    '''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dct = {}
        filter_on = 0

        if type(attrs) is list:
            for attr in attrs:
                if attr in self.__dict__:
                    dct.update({attr: self.__dict__[attr]})
                    filter_on = 1
            if filter_on:
                return dct

        return self.__dict__
