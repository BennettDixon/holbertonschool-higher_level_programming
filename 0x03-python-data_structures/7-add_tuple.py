#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """
    adds the first two elements of two tuples together
    and returns the result
    """
    ta_len = len(tuple_a)
    tb_len = len(tuple_b)
    new_tup = ()
    for i in range(2):
        if i >= ta_len:
            val_a = 0
        else:
            val_a = tuple_a[i]
        if i >= tb_len:
            val_b = 0
        else:
            val_b = tuple_b[i]

        if (i == 0):
            new_tup = (val_a + val_b)
        else:
            new_tup = (new_tup, val_a + val_b)

    return (new_tup)
