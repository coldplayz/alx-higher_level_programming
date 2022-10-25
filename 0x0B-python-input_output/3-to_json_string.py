#!/usr/bin/python3
'''Module for serialization to JSON.
'''
import json


def to_json_string(my_obj):
    '''Returns the JSON representation of my_obj.

    Args:
        my_obj (object): an object to be serialized.

    Returns:
        str: the JSON representation of my_obj.
    '''

    return json.dumps(my_obj)
