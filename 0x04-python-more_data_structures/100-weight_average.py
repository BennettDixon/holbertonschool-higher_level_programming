#!/usr/bin/python3


def weight_average(my_list=[]):
    avg = 0
    scores = [score*weight for (score, weight) in my_list]
    print(scores)
    return sum(scores) / sum([weight for (score, weight) in my_list])
