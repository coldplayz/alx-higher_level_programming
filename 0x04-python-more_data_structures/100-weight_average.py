#!/usr/bin/python3

def weight_average(my_list=[]):
    '''Returns the weighted average of all integers tuple (score, weight)'''

    if len(my_list) == 0 or my_list is None:
        return 0

    gsum = 0
    wsum = 0
    for tup in my_list:
        gsum += tup[0] * tup[1]
        wsum += tup[1]

    return (float(gsum) / wsum)
