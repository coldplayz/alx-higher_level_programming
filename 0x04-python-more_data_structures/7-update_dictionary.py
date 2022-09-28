#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    '''Replaces or adds key/value in a dictionary'''

    upd = {key: value}
    if a_dictionary is None:
        return upd

    a_dictionary.update(upd)

    return a_dictionary
