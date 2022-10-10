#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    '''prints an integer with error message on exception'''

    try:
        print("{:d}".format(value))
        return True
    except TypeError as te:
        print("Exception: {}".format(te.args[0]), file=sys.stderr)
        return False
    except ValueError as ve:
        print("Exception: {}".format(ve.args[0]), file=sys.stderr)
        return False
