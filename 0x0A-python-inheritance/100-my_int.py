#!/usr/bin/python3
'''Module of the rebel class.
'''


class MyInt(int):
    '''Subclass of int.
    '''

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
