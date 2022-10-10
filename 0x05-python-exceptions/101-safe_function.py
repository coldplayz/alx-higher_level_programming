#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    '''defines a function safely'''

    try:
        res = fct(*args)
        return res
    except BaseException as exc:
        print("Exception: {}".format(exc.args[0]), file=sys.stderr)
        return None
