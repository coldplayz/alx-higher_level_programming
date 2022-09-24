#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    '''prints a matrix of integers'''

    size = len(matrix[0])
    if size == 0:
        print()

    for elem in matrix:
        elem_size = len(elem)
        if elem_size == 0:
            continue
        for i in range(elem_size):
            d = elem[i]
            print("{:d}".format(d), end='\n' if i == (elem_size - 1) else ' ')
