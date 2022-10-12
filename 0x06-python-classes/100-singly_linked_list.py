#!/usr/bin/python3
'''Module for creating singly-linked lists'''


class Node:
    '''Creates a Node class'''

    def __init__(self, data, next_node=None):
        self.data = data  # automatically checked by property
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        '''sets the data attribute'''
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None or type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    '''creates a class for singly-linked lists'''

    def __init__(self, 
