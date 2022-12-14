#!/usr/bin/python3
'''
Module for Mylist class.
'''


class MyList(list):
    '''
    Subclass of list for sorted print.
    '''

    def print_sorted(self):
        '''
        Prints a sorted list.
        '''

        print(sorted(self))
