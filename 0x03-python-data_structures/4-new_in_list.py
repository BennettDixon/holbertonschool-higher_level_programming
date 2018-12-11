#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific position
    Without modifying the original list
    """
    l_len = len(my_list)
    if idx >= l_len or idx < 0:
        return (my_list)

    new_list = my_list[:]
    new_list[idx] = element
    return (new_list)
