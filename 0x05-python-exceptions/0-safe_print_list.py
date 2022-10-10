#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    '''Safely prints the elements of a list and returns the number printed'''

    np = 0

    for i in range(x):
        try:
            print(my_list[i], end='')
            np += 1
        except IndexError:
            break;
    print()

    return np
