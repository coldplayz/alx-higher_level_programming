#!/usr/bin/python3
'''
Module to print a formal introduction.
'''


def say_my_name(first_name, last_name=""):
    '''Prints a formal name introduction.

    Args:
        first_name (str): a string
        last_name (str): a string

    Raises:
        TypeError: if first_name and/or last_name is not a string object.
    '''

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is", first_name, last_name)
