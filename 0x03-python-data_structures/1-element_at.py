#!/usr/bin/python3


def element_at(my_list, idx):
    """
    Gets an element in a list at given index
    And returns it
    """
    list_len = len(my_list)
    if idx >= list_len or idx < 0:
        return

    return (my_list[idx])
