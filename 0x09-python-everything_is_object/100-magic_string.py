#!/usr/bin/python3

class Counter():
    i = 0

def magic_string():
    string = ""
    Counter.i += 1
    for i in range(0, Counter.i):
        string += "Holberton"
        if i != Counter.i - 1:
            string += ", "
    return string
