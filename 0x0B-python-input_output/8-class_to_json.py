#!/usr/bin/python3
'''Module for serialization without JSON.
'''


def class_to_json(obj):
    '''Returns a dictionary description of obj.

    Args:
        obj (object): an instance of a class.

    Returns:
        dict: description of attributes of obj.
    '''

    dct = {}

    if '__dict__' in dir(obj):
        return obj.__dict__

    return dct
