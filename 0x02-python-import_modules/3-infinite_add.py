#!/usr/bin/python3

import sys

c = len(sys.argv)


def add_all():
    '''Adds all command-line arguments'''
    summ = 0
    for i in range(1, c):
        summ += int(sys.argv[i])
    print("{:d}".format(summ))


if __name__ == "__main__":
    add_all()
