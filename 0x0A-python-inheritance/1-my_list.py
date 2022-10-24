#!/usr/bin/python3
'''Module for Mylist class.
'''


class Mylist(list):
    '''Subclass of list for sorted print.
    '''

    def print_sorted(self):
        print(sorted(self))
