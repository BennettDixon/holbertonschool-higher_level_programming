#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """
    prints a matrix of integers to STDOUT
    """
    for i in range(len(matrix)):
        subm_len = len(matrix[i])
        for j in range(subm_len):
            if j != subm_len - 1:
                endCh = ' '
            else:
                endCh = ''
            print("{:d}".format(matrix[i][j]), end=endCh)
        print("")
