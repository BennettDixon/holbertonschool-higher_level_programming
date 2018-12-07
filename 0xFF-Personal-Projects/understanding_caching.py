#!/usr/bin/python3


def comp_print(val1, val2):
    print("a:{}\nb:{}".format(id(a), id(b)))
    if a is b:
        print("a is b for {} & {}".format(a, b))
    if a == b:
        print("a == b for {} & {}".format(a, b))

a = "abc"
b = "abc"
comp_print(a, b)

a = 'abc abc'
id(a)
b = 'abc abc'
comp_print(a, b)
