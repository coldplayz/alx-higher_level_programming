#!/usr/bin/python3
'''Module for appending to a file.
'''


def append_write(filename="", text=""):
    '''Appends text to filename.

    Args:
        filename (str): a file path name.
        text (str): the string to write.

    Returns:
        int: number of characters appended.
    '''

    with open(filename, 'a', encoding='utf-8') as fout:
        if type(text) is str:
            written = fout.write(text)
            return written
