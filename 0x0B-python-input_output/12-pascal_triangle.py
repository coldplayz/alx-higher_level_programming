#!/usr/bin/python3
'''Module for Pascal's traingle.
'''


def pascal_triangle(n):
    '''Returns a list of lists representing Pascal's triangle of n.

    Args:
        n (int): the size of the triangle.

    Returns:
        list: a list of lists of the triangle.
    '''

    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        # Initilaize the triangle with empty lists
        triangle.append([])

    # Fill the first two lists
    triangle[0].append(1)  # triangle[0] == [1]
    if n == 1:
        return triangle

    triangle[1].append(1)  # triangle[1] == [1]
    triangle[1].append(1)  # triangle[1] == [1, 1]
    if n == 2:
        return triangle

    # Compute the other lists
    for t_idx in range(2, n):
        # Start from the third list as first two have been filled already
        cur_list_len = len(triangle[t_idx - 1]) + 1
        for l_idx in range(cur_list_len):
            # Use length of previous list plus one for current list
            if l_idx == 0 or l_idx == cur_list_len - 1:
                # At first or last index
                triangle[t_idx].append(1)
            else:
                # Sum up the last two values of the previous list, and append
                val = triangle[t_idx - 1][l_idx] +\
                        triangle[t_idx - 1][l_idx - 1]
                triangle[t_idx].append(val)

    return triangle
