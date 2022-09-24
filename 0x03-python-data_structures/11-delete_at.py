#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    '''Deletes the item at idx'''

    size = len(my_list)
    if idx < 0 or idx >= size:  # out of bounds
        return my_list

    del my_list[idx]
    return my_list
