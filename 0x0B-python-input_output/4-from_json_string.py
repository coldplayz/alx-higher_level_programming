#!/usr/bin/python3
'''Module for deserialization.
'''
import json


def from_json_string(my_str):
    '''Returns the Python object equivalent of my_str.

    Args:
        my_str (str): JSON string to deserialize.

    Returns:
        object: a Python object.
    '''

    return json.loads(my_str)
