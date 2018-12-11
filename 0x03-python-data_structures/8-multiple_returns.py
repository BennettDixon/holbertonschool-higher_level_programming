#!/usr/bin/python3


def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first
    character
    """
    s_len = len(sentence)
    if s_len == 0:
        f_char = None
    else:
        f_char = sentence[0]
    return ((s_len, f_char))
