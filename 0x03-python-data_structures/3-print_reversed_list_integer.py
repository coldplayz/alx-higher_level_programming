#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    '''Prints integers in my_list, in reverse'''

    if my_list is None:
        return
    my_list.reverse()  # reverse my_list

    for i in my_list:
        print("{:d}".format(i))
