#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    sign = "is negative"
elif number > 0:
    sign = "is positive"
else:
    sign = "is zero"
print("{:d}".format(number), sign)
