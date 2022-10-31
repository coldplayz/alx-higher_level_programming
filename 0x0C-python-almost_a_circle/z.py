#!/usr/bin/python3

class A:
    var = 0
    def __init__(self):
        self.__class__.var += 1

class B(A):
    def __init__(self):
        super().__init__()
