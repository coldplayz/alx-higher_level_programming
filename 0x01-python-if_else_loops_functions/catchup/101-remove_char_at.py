#!/usr/bin/python3

def remove_char_at(strr, n):
    '''Removes the char at index n in strr'''
    cpy = strr[: n] + strr[n+1 :]
    return cpy
