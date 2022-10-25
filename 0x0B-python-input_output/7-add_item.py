#!/usr/bin/python3
'''Module for serializing to file.
'''
import json
import sys


def save_to_json_file(my_obj, filename):
    '''Serializes my_obj into filename.

    Args:
        my_obj (object): object to serialize.
        filename (str): file path name.
    '''

    with open(filename, 'w', encoding='utf-8') as fout:
        json.dump(my_obj, fout)


def load_from_json_file(filename):
    '''Creates a Python object from a JSON file.

    Args:
        filename (str): a file path name.

    Returns:
        object: a Python object.
    '''

    with open(filename, 'r', encoding='utf-8') as fin:
        return json.load(fin)


args_list = []
json_file = "add_item.json"

try:
    arr = load_from_json_file(json_file)
except FileNotFoundError:
    arr = []

for idx in range(1, len(sys.argv)):
    args_list.append(sys.argv[idx])

arr.extend(args_list)

save_to_json_file(arr, json_file)
