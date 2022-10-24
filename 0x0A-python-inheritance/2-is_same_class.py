#!/usr/bin/python3
'''Module to check exact type.
'''


def is_same_class(obj, a_class):
    '''Checks if obj is an exact instance of a_class.

    Args:
        obj (object): any object.
        a_class (type): any class.

    Returns:
        bool: True if obj is an exact instance of a_class, and False otherwise
    '''

    return type(obj) is a_class
