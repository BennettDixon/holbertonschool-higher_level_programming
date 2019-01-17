#!/usr/bin/python3


def pascal_triangle(n):
    """gets pascal triangle for n,
        -> n assumed to always be int
        -> handles NO exceptions
       Return: matrix of list of values representing triangle
    """
    ret_mat = []
    for i in range(0, n):
        mat_len = len(ret_mat)
        if mat_len <= 1:
            ret_mat.append([1 for q in range(0, mat_len + 1)])
        else:
            new_row = []
            for j in range(0, len(ret_mat[i - 1]) + 1):
                if j == 0 or j == len(ret_mat[i - 1]):
                    new_row.append(1)
                else:
                    new_row.append(ret_mat[i - 1][j - 1] + ret_mat[i - 1][j])
            ret_mat.append(new_row)
    return ret_mat
