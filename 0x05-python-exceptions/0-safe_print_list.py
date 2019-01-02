#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    i = 0
    list_len = 0
    for ele in my_list:
        list_len += 1
    if (x > list_len):
        x = list_len
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
        print()
    except:
        print(end="")
    finally:
        return i + 1
