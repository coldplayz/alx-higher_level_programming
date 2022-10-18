#!/usr/bin/python3
'''
Class LockedClass.
'''


class LockedClass:
    '''Creates a class that rejects new attributes.
    '''

    def __setattr__(self, key, value):
        if key != 'first_name':
            raise AttributeError(
                    f"'{self.__class__.__name__}'" +
                    f" object has no attribute '{key}'")
        object.__setattr__(self, key, value)
