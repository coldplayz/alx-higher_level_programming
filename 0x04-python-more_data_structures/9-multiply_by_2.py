#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    '''Returns a new dictionary with double the original values'''

    if a_dictionary is None:
        return None

    dictcpy = a_dictionary.copy()

    for key in dictcpy.keys():
        dictcpy[key] = (dictcpy[key]) * 2

    return dictcpy
