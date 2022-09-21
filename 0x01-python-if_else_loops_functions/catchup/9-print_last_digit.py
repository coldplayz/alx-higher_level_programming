#!/usr/bin/python3

def print_last_digit(number):
    '''prints and returns the last digit of number'''
    neg2pos = -1

    if number < 0:
        neg2pos = number * (-1)
        neg2pos = neg2pos % 10

    last = number % 10

    if neg2pos != -1:
        print(f"{neg2pos}", end='')  # number is negative
        return neg2pos
    else:
        print(f"{last}", end='')
        return last
