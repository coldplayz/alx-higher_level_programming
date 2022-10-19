#!/usr/bin/python3

'''
Module for dividing a matrix.
'''


def matrix_divided(matrix, div):
    '''Divides all elements of a matrix

    Args:
        matrix (list): list of lists of integers/floats
        div (int or float): the divisor

    Returns:
        list: a new list object.

    Raises:
        TypeError: if ``matrix`` is not a list of lists of integers, or floats;
            and/or ``div`` is not an int or float object.
        ZeroDivisionError: if ``div`` is equal to zero.
    '''

    if type(matrix) is not list:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    for ar in matrix:
        # At least one item in matrix
        if type(ar) is not list:
            raise TypeError(
                    "matrix must be a matrix " +
                    "(list of lists) of integers/floats")
        matrix0_len = len(matrix[0])
        for i in ar:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix " +
                                "(list of lists) of integers/floats")
        if matrix0_len != len(ar):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Implement deep copy of matrix
    mcopy = []
    for ar in matrix:
        mcopy.append(ar.copy())

    # Implement matrix division
    for ar in mcopy:
        for i in range(len(ar)):
            ar[i] = round(float(ar[i]) / div, 2)

    return mcopy
