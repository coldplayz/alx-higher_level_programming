#!/usr/bin/python3
'''Module for reading and printing a UTF-8 text file.
'''


def read_file(filename=""):
    '''Reads and prints from filename.

    Args:
        filename (str): file path name.
    '''

    with open(filename, encoding='utf-8') as fobj:
        txt = fobj.read()

    print(txt, end='')
