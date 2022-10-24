#!/usr/bin/python3
'''Module to check for subclassness.
'''


def inherits_from(obj, a_class):
    '''Checks if type of obj is a subclass of a_class.

    Args:
        obj (object): any object.
        a_class (type): class object.

    Returns:
        bool: True if type(obj) is a subclass of a_class.
    '''

    if type(obj) is a_class:
        return False

    return issubclass(type(obj), a_class)
