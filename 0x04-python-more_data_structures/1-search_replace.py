#!/usr/bin/python3

def search_replace(my_list, search, replace):
    '''Changes all occurences of search to replace in my_list'''

    if my_list is None:
        return my_list

    listcpy = my_list.copy()

    if search is None:
        for i in range(len(listcpy)):
            if listcpy[i] is search:  # compare for reference to same object
                listcpy[i] = replace
    else:
        for i in range(len(listcpy)):
            if listcpy[i] == search:  # compare for equality of value
                listcpy[i] = replace

    return listcpy
