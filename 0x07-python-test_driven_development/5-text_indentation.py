#!/usr/bin/python3
'''
Module for ``text_indentation()``
'''


def text_indentation(text):
    '''Prints a text with two lines after
    every occurence of ``.``, ``?``, and ``:`` characters.

    Args:
        text (str): a string.

    Raises:
        TypeError: if ``text`` is not a string object
        ValueError: if a key does not exist in a dictionary.
    '''

    if type(text) is not str:
        raise TypeError("text must be a string")

    t1 = text
    t2 = ""

    mapp = {'dot': None, 'que': None, 'col': None}

    dot, que, col = (1, 1, 1)
    while True:
        try:
            if dot:  # key 'dot' still exists in dictionary, mapp
                mapp['dot'] = t1.index('.')
        except ValueError:  # character does not exist [anymore]
            if len(mapp) != 1:
                del mapp['dot']
                dot = 0
            else:
                # mapp has only one item
                t1 = t1.strip(' ')
                t2 += t1
                print(t2, end='')
                return

        try:
            if que:
                mapp['que'] = t1.index('?')
        except ValueError:
            if len(mapp) != 1:
                del mapp['que']
                que = 0
            else:
                t1 = t1.strip(' ')
                t2 += t1
                print(t2, end='')
                return

        try:
            if col:
                mapp['col'] = t1.index(':')
        except ValueError:
            if len(mapp) != 1:
                del mapp['col']
                col = 0
            else:
                t1 = t1.strip(' ')
                t2 += t1
                print(t2, end='')
                return

        # get index of nearest occurence of a special character
        slice_idx = mapp[list(mapp.keys())[0]]  # value of first key is basis
        for val in mapp.values():
            slice_idx = val if val < slice_idx else slice_idx

        # concat slice including special character
        slc = (t1[: slice_idx + 1] + "\n\n").strip(" ")
        t2 += slc
        t1 = t1[slice_idx + 1:]  # update t1 to exclude concatenated slice
