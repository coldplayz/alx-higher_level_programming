#!/usr/bin/python3
'''Module for writing to a file.
'''


def write_file(filename="", text=""):
    '''Writes text to filename.

    Args:
        filename (str): a file path name.
        text (str): the string to write.

    Returns:
        int: number of characters written.
    '''

    with open(filename, 'w', encoding='utf-8') as fout:
        if type(text) is str:
            written = fout.write(text)
            return written
