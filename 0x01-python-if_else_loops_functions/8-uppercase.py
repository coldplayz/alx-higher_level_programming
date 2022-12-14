#!/usr/bin/python3

def islower(c):
    '''Checks if c is lowercase'''
    if 97 <= ord(c) <= 122:
        return True
    else:
        return False


def isupper(c):
    '''Checks if c is uppercase'''
    if 65 <= ord(c) <= 90:
        return True
    else:
        return False


def uppercase(strr):
    '''Prints str in uppercase'''
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counter = 0

    if len(strr) == 0:  # for empty strr; to allow loop entrance
        strr = '\n'
    for i in strr:
        if islower(i):
            i = "{}".format(upper[ord(i) - 97])
        if counter == (len(strr) - 1):  # at strr end
            print("{}".format(strr if strr[0] == '\n' else i + '\n'), end='')
        else:
            print("{}".format(i), end='')
        counter += 1
