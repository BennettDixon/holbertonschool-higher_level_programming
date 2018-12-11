#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    """
    deletes an element from a list at a given index
    """
    l_len = len(my_list)
    if idx >= l_len or idx < 0:
        return (my_list)

    del my_list[idx]
    return (my_list)
