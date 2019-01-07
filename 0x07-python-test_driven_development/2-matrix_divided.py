#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix, elements must be ->
        int or float type
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
        return matrix
    elif div == 0:
        raise ZeroDivisionError("division by zero")
        return matrix

    prevRowLen = -1
    new_list = []
    for row in matrix:
        if (prevRowLen != len(row) and prevRowLen != -1):
            raise TypeError("Each row of the matrix must have the same size")
            return matrix
        for ele in row:
            if not isinstance(ele, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of" +
                                " integers/floats")
                return matrix
            else:
                new_list.append(round(ele / div, 2))
        prevRowLen = len(row)

    return new_list
