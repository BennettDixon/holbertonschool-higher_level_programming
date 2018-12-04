#!/usr/bin/python3


def remove_char_at(str, n):
    i = 0
    newStr = ""
    for c in str:
        if i != n:
            newStr += c
        i += 1
    return (newStr)
