#!/usr/bin/python3

def common_elements(set_1, set_2):
    '''Returns the intersection of two sets'''

    if set_1 is None or set_2 is None:
        return set()

    return (set_1 & set_2)
