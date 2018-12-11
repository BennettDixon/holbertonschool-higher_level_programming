#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """
    finds all multiples of 2 in a list and returns
    a list containing True / False repsective to index
    """
    list_len = len(my_list)
    if list_len == 0:
        return None

    bool_list = []
    for i in range(list_len):
        if my_list[i] % 2 == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)
    return (bool_list)
