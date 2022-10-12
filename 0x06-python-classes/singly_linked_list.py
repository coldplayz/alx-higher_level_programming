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
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    '''creates a class for singly-linked lists'''

    def __init__(self):
        self.__head = None  # __head to reference Node instances

    def sorted_insert(self, value):
        '''adds a new node to the list'''
        self.__head = Node(value, self.__head)  # node added at beginning
        '''To implement node-adding at list end,
        do not pass head for instantiation above, only value.
        '''

        self.__ptr1 = self.__head
        if self.__ptr1:
            self.__ptr2 = self.__ptr1.__next_node
        else:
            return

        if self.__ptr1.__data < self.__ptr2.__data:
            return

        # save reference to previous head
        self.__prev_head = self.__head.__next_node
        while self.__ptr2:
            if self.__head.__data < self.__ptr2.__data:
                # insert __head between ptr1 and ptr2
                self.__ptr1.__next_node = self.__head  # node ptr1 -> head
                self.__head.__next_node = self.__ptr2  # head -> node ptr2
                self.__head = self.__prev_head  # assign new head
                return

            # move pointers forwards
            self.__ptr1 = self.__ptr2
            self.__ptr2 = self.__ptr2.__next_node

        # ptr2 now None; insert head at list tail
        self.__ptr1.__next_node = self.__head
        self.__head.__next_node = None

        # assign new head
        self.__head = self.__prev_head

    def __str__(self):
        strr = ""
        self.__tmp = self.__head
        while self.__tmp:
            strr += str(self__tmp.__data) +\
                    "" if self.__tmp.__next_node is None else "\n"
            self.__tmp = self.__tmp.__next_node

        return strr
