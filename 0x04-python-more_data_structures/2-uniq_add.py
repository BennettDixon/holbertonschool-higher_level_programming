#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    adds all unique elements of a list of ints together
    """
    return (sum({ele for ele in my_list}))
