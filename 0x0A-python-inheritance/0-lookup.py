#!/usr/bin/python3
'''
Module for object lookup.
'''


def lookup(obj):
    '''Returns a list of obj's attributes.

    Args:
        obj (object): any object.

    Returns:
        list: a list of attributes of obj.
    '''

    arr = []

    try:
        arr = dir(obj)
        return arr
    except AttributeError:
        pass

    return arr
