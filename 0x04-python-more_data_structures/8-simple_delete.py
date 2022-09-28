#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    '''Deletes key in a_dictionary'''

    if a_dictionary is None:
        return None

    if key not in a_dictionary:
        return a_dictionary

    del a_dictionary[key]

    return a_dictionary
