#!/usr/bin/python3


def matrix_mul(m_a, m_b):
    """
    produces a result of matrix multiplaction of two matricies
    checks for bad input to function
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not check_list_of_lists(m_a):
        raise TypeError("m_a must be a list of lists")
    if not check_list_of_lists(m_b):
        raise TypeError("m_b must be a list of lists")

    if not check_empty_list(m_a):
        raise ValueError("m_a can't be empty")
    if not check_empty_list(m_b):
        raise ValueError("m_b can't be empty")

    if not check_ele_types(m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not check_ele_types(m_b):
        raise TypeError("m_b should contain only integers or floats")

    if not check_rectangle(m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not check_rectangle(m_b):
        raise TypeError("each row of m_a must should be of the same size")

    if not check_matrix_mult(m_a, m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    if len(m_a) > len(m_b[0]):
        res_len = len(m_a)
    elif len(m_a) < len(m_b[0]):
        res_len = len(m_b[0])
    else:
        res_len = len(m_a)

    new_matrix = []
    for row_i in range(0, len(m_a)):
        values = []
        for col_i in range(0, len(m_b[0])):
            res = 0
            for j in range(0, len(m_a[row_i])):
                res += m_a[row_i][j] * m_b[j][col_i]
            values.append(res)
        new_matrix.append(values)
    return new_matrix


def check_matrix_mult(m_a, m_b):
    """checks that two matricies can infact be multiplied
       length of row of m_a is equal to columns (num rows) in m_b
       all other matricies checks assumed to have been done
    """
    return (len(m_a) == len(m_b[0]) or len(m_b) == len(m_a[0]))


def check_list_of_lists(matrix):
    """checks if a list is a list of lists (aka a matrix)
    """
    for row in matrix:
        if not isinstance(row, list):
            return False
    return True


def check_ele_types(matrix):
    """checks if a matrix (list of lists) contains non ints/floats
    """
    for row in matrix:
        for ele in row:
            if not isinstance(ele, (int, float)):
                return False
    return True


def check_empty_list(m):
    """checks if the matrix is empty of sub matrix is empty
    """
    if ((m is None or len(m) == 0) or (m[0] is None or len(m[0]) == 0)):
        return False
    return True


def check_rectangle(matrix):
    """checks if a matrix is a rectangle
    """
    prevRowSize = -1
    for row in matrix:
        if prevRowSize != -1 and prevRowSize != len(row):
            return False
        prevRowSize = len(row)
    return True
