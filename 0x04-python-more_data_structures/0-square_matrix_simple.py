#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    '''Returns the square of matrix'''

    if matrix is None or len(matrix) == 0:
        return matrix

    mcopy = []
    for i in range(len(matrix)):  # make copies of inner lists
        mcopy.append(matrix[i].copy())

    for ar in mcopy:
        for i in range(len(ar)):
            ar[i] = (ar[i]) ** 2

    return mcopy
