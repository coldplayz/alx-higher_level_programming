#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    '''Returns the set of elements exclusively present in set_1 and set_2'''

    if set_1 is None or set_2 is None:
        return set()

    return (set_1 ^ set_2)
