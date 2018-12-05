#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

argc = len(sys.argv) - 1

i = 0
result = 0
for arg in sys.argv:
    if i != 0:
        result += int(arg)
    else:
        i += 1
print("{:d}".format(result))
