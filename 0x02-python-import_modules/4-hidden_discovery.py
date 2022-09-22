#!/usr/bin/python3

import hidden_4

arr = dir(hidden_4)
n = len(arr)


def print_names():
    '''Print list items'''
    for i in range(n):
        if arr[i][0:2] != "__":
            print(arr[i])


if __name__ == "__main__":
    print_names()
