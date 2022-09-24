#!/usr/bin/python3

def no_c(my_string):
    '''Removes c or C char from my_string'''

    new_str = ''  # init string to return
    charlist = [c for c in my_string if 'C' != c != 'c']  # filter out c/C

    for c in charlist:
        new_str += c  # compose the required string
    return new_str
