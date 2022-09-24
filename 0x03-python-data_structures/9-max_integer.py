#!/usr/bin/python3

def max_integer(my_list=[]):
    '''Returns the biggest integer in a list'''

    size = len(my_list)
    if size == 0:
        return None

    d = my_list[0]
    for i in my_list:
        if i > d:
            d = i

    return d
