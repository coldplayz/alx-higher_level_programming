#!/usr/bin/python3
'''Module for serializing to file.
'''
import json


def save_to_json_file(my_obj, filename):
    '''Serializes my_obj into filename.

    Args:
        my_obj (object): object to serialize.
        filename (str): file path name.
    '''

    with open(filename, 'w', encoding='utf-8') as fout:
        json.dump(my_obj, fout)
