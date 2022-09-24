#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    '''finds all multiples of 2 in a list'''

    size = len(my_list)
    if size == 0:
        return my_list

    my_list2 = my_list.copy()  # so as not to modify original
    for i in range(size):
        if my_list[i] % 2 == 0:
            my_list2[i] = True
        else:
            my_list2[i] = False

    return my_list2
