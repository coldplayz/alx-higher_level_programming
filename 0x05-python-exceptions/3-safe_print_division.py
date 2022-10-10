#!/usr/bin/python3

def safe_print_division(a, b):
    '''divides 2 integers and prints the result'''

    flag = 0
    try:
        res = a / b
        flag = 1
        return res
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(res if flag == 1 else None))
