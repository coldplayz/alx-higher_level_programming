#!/usr/bin/python3

def remove_char_at(strr, n):
    '''Removes the char at index n in strr'''
    if n >= 0:
        cpy = strr[:n] + strr[n+1:]
        return cpy
    return strr
