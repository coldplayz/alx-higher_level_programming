#!/usr/bin/python3
'''Module for setting attributes safely.
'''


def add_attribute(obj, name, value):
    '''Safely binds an attribute to an object.

    Args:
        obj (object): an object.
        name (str): attribute name.
        value (str): attribute value.
    '''

    dir_list = dir(obj)

    if '__dict__' in dir_list:
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
