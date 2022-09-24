#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    '''Adds two tuples and returns a two-item tuple'''

    # parse both tuples
    ta_len = len(tuple_a)  # for tuple_a
    if ta_len == 0:
        tuple_a = (0, 0)
    elif ta_len == 1:
        tuple_a += (0,)

    tb_len = len(tuple_b)  # for tuple_b
    if tb_len == 0:
        tuple_b = (0, 0)
    elif tb_len == 1:
        tuple_b += (0,)

    new_tuple = ()

    # compose new tuple
    for i in range(2):
        new_tuple += (tuple_a[i] + tuple_b[i],)

    return new_tuple
