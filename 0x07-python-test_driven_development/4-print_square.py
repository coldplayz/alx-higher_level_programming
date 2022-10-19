#!/usr/bin/python3
'''
Module to print_squares.
'''


def print_square(size):
    '''Prints squares using the character ``#``.

    Args:
        size (int): a positive integer.
    '''

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")

    if size > 0:
        for i in range(size):
            for j in range(size):
                print('#', end='')
            print()
    else:
        # size == 0
        print('\n', end='')
