#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """
    returns a set of all elements present in only one set
    """
    new_set = set_1 | set_2
    return {ele for ele in new_set if ele in set_1 and ele not in set_2 or
            ele in set_2 and ele not in set_1}
