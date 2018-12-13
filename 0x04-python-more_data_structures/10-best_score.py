#!/usr/bin/python3


def best_score(a_dictionary):
    """
    gets the best value from a dictionary (greatest integer)
    """
    win_n = 0
    winner = None
    if type(a_dictionary) is dict:
        for (key, value) in a_dictionary.items():
            if value > win_n:
                win_n = value
                winner = key
    return winner
