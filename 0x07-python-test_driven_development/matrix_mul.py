#!/usr/bin/python3
'''
Module for ``matrix_mul()``.
'''


def matrix_mul(m_a, m_b):
    '''Multiplies two matrices.

    Args:
        m_a (list): a list of lists.
        m_b (list): a matrix like m_a.

    Returns:
        list: the product of m_a and m_b.
    '''

    # Argument validations
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if len(m_a):
        for seq in m_a:
            if type(seq) is not list:
                raise TypeError("m_a must be a list of lists")
    if len(m_b):
        for seq in m_b:
            if type(seq) is not list:
                raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise TypeError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise TypeError("m_b can't be empty")

    for elem in m_a:
        for num in elem:
            if type(num) is not int and type(num) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for elem in m_b:
        for num in elem:
            if type(num) is not int and type(num) is not float:
                raise TypeError("m_b should contain only integers or floats")

    size = len(m_a[0])
    for seq in m_a:
        if len(seq) != size:
            raise TypeError("each row of m_a must be of the same size")
    size = len(m_b[0])
    for seq in m_b:
        if len(seq) != size:
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        # number of columns in m_a not equal to number of rows in m_b
        # m_a not conformable to m_b for multiplication
        raise ValueError("m_a and m_b can't be multiplied")

    # Mulltiplication implementation
    result = []

    for ma_row_idx in range(len(m_a)):
        # iteration == number of rows to be in result
        new_row = []
        for j in m_a[ma_row_idx]:
            # init new_row with zero
            new_row.append(0)

        for i in range(len(m_b[0])):
            # iteration == number of columns to be in result
            fact2_list = []  # factor one is m_a[ma_row_idx]
            # Populate fact2_list with data from m_b
            for mb_row in m_b:
                fact2_list.append(mb_row[i])

            for i2 in range(len(fact2_list)):
                # update columns in new_row
                new_row[i] += m_a[ma_row_idx][i2] * fact2_list[i2]

        result.append(new_row)

    return result
