#!/usr/bin/python3

def multiple_returns(sentence):
    '''returns a tuple with the length of a string and its first character.'''

    tup = ()
    size = len(sentence)
    if size == 0:
        tup += (0, None)
        return tup

    tup += (size, sentence[0])
    return tup
