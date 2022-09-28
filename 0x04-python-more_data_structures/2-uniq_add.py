#!/usr/bin/python3

def uniq_add(my_list=[]):
    '''Adds all unique integers in a list'''

    if my_list is None:
        return None

    lset = set(my_list)  # use set to remove duplicates
    setl = list(lset)  # compose back to a list

    summ = 0
    for i in setl:
        summ += i

    return summ
