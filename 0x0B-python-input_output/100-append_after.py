#!/usr/bin/python3
'''Module for updating a file.
'''


def append_after(filename="", search_string="", new_string=""):
    '''Adds a new line of text after line containing search_string.

    Args:
        filename (str): a file path name.
        search_string (str): string to search for.
        new_string (str): string to add to file.
    '''

    with open(filename, 'r', encoding='utf-8') as f:
        file = f.readlines()
        idx = 0

        file_cpy = file.copy()
        for line in file_cpy:
            if search_string in line:
                file.insert(idx + 1, new_string)
                idx += 1
            idx += 1

    with open(filename, 'w', encoding='utf-8') as f:
        for line in file:
            f.write(line)
