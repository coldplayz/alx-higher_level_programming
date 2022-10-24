#!/usr/bin/python3
'''
Module for checking instanceship.
'''


def is_kind_of_class(obj, a_class):
    '''Checks if obj is a loose instance of a_class.

    Args:
        obj (object): any object.
        a_class (type): any class object.

    Returns:
        bool: True if obj is an instance of a_class, else False.
    '''

    return isinstance(obj, a_class)
