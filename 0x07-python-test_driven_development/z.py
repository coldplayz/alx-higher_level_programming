#!/usr/bin/python3

def text_indentation(text):
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
                t2 += t1
                print(t2, end='')
                return

        # get index of nearest occurence of a special character
        slice_idx = mapp[list(mapp.keys())[0]]  # value of first key is basis
        for val in mapp.values():
            slice_idx = val if val < slice_idx else slice_idx

        # concat slice including special character
        t2 += t1[: slice_idx + 1] + "\n\n"
        t1 = t1[slice_idx + 1:]  # update t1 to exclude concatenated slice


text_indentation("str.in:g")
