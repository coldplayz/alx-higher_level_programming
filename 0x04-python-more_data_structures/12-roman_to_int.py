#!/usr/bin/python3

def roman_to_int(roman_string):
    '''Converts roman numerals to integers'''

    if type(roman_string) != str or roman_string is None:
        return 0

    rdict = dict(
            I=1, i=1, V=5, v=5, X=10, x=10, L=50, l=50, C=100,
            c=100, D=500, d=500, M=1000, m=1000)

    summ = 0
    flag = False
    for i in range(len(roman_string)):
        if flag:
            flag = False
            continue  # skip adding current value as its already added
        if i < len(roman_string) - 1:
            if rdict[roman_string[i + 1]] > rdict[roman_string[i]]:
                flag = True  # next loop will be continued
                summ += rdict[roman_string[i + 1]] - rdict[roman_string[i]]
            else:
                summ += rdict[roman_string[i]]
        else:
            summ += rdict[roman_string[i]]  # for the last numeral character

    return summ
