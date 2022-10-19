#!/usr/bin/python3

'''
Module for adding two integers
'''


def add_integer(a, b=98):
    '''Returns the sum of two integers.

    Args:
        a (int or float): a number.
        b (int or float, optional): a number

    Returns:
        int: sum of a and b
    '''

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
