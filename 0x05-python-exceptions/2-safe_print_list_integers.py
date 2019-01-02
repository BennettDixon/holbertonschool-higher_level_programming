#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    prints a list of anything, but only prints the integers
    Returns the amount of integers printed
    """
    i = 0
    printed = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed += 1
        except (ValueError, TypeError):
            continue
    print()
    return printed
