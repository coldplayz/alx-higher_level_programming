#!/usr/bin/python3

import sys

c = len(sys.argv) - 1

if __name__ == "__main__":
    print("{} {}".format(c, "argument" if c == 1 else "arguments"), end='')
    print("{}".format("." if c == 0 else ":"))

    for i in range(1, c + 1):
        print("{}: {}".format(i, sys.argv[i]))
