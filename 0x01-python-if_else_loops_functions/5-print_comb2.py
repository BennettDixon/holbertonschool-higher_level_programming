#!/usr/bin/python3
endStr = ", "

for i in range(0, 100):
    if i == 99:
        endStr = ""
    print("{:02d}".format(i), end=endStr)
print('')
