#!/usr/bin/python3

def best_score(a_dictionary):
    '''Returns key with biggest integer value'''

    if a_dictionary is None:
        return None

    keylist = list(a_dictionary.keys())

    bigkey = keylist[0]
    for key in a_dictionary.keys():
        # assign the key with the biggest value to bigkey
        bigkey = bigkey if a_dictionary[bigkey] >= a_dictionary[key] else key

    return bigkey
