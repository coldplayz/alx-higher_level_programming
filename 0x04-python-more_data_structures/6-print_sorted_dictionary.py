#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    '''Prints a dictionary by ordered keys'''

    if a_dictionary is None:
        return

    okeys = sorted(list(a_dictionary.keys()))  # list of ordered keys

    for i in range(len(a_dictionary)):
        print("{}:".format(okeys[i]), a_dictionary[okeys[i]])
