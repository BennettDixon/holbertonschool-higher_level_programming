#!/usr/bin/python3


def uppercase(str):
    for c in str:
        temp = ord(c)
        if temp >= 97 and temp <= 122:
            temp -= 32
        print("{:c}".format(temp), end='')
    print()
