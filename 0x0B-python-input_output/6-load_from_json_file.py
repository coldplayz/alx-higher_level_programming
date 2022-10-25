#!/usr/bin/python3
'''Module for deserializing from file.
'''
import json


def load_from_json_file(filename):
    '''Creates a Python object from a JSON file.

    Args:
        filename (str): a file path name.

    Returns:
        object: a Python object.
    '''

    with open(filename, 'r', encoding='utf-8') as fin:
        return json.load(fin)
