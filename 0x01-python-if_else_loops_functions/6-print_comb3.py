#!/usr/bin/python3

shift = 0

for i in range(9):
    shift += 1
    for j in range(i * 10 + shift, i * 10 + 10):
        if j == 89:
            print(89)
        else:
            print("{:02d}, ".format(j), end='')

