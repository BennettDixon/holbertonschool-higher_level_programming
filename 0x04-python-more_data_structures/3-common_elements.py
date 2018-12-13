#!/usr/bin/python3


def common_elements(set_1, set_2):
    """
    returns a set of common elements from two sets
    """
    return ({ele for ele in set_1 if ele in set_2})
