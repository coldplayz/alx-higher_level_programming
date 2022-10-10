#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    '''divides element by element 2 lists'''

    newlist = []

    for i in range(list_length):
        zero = 1
        try:
            quot = my_list_1[i] / my_list_2[i]
            newlist.append(quot)
            zero = 0
        except ZeroDivisionError:
            print("division by 0")
        except (TypeError, ValueError):
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            if zero:
                newlist.append(0)

    return newlist
