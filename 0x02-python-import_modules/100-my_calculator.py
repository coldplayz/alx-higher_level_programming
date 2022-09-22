#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys

c = len(sys.argv)


def handle_op():
    '''Handles command-line-specified operations'''

    if c != 4:  # including the script's name specified
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    av1 = sys.argv[1]
    op = sys.argv[2]  # operator string
    av3 = sys.argv[3]
    a1 = int(av1)
    a3 = int(av3)

    if op == '-' or op == '+' or op == '*' or op == '/':
        pass
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if op == '-':
        print("{} {} {} = {}".format(int(av1), op, int(av3), sub(a1, a3)))
    elif op == '+':
        print("{} {} {} = {}".format(int(av1), op, int(av3), add(a1, a3)))
    elif op == '*':
        print("{} {} {} = {}".format(int(av1), op, int(av3), mul(a1, a3)))
    else:
        print("{} {} {} = {}".format(int(av1), op, int(av3), div(a1, a3)))


if __name__ == "__main__":
    handle_op()
