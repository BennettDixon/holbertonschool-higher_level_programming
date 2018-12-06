#!/usr/bin/python3


def uppercase(str):
    cap_str = ""
    for c in str:
        temp = ord(c)
        if temp >= 97 and temp <= 122:
            temp -= 32
        cap_str += chr(temp)
    print(cap_str)
