#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        number = -(number)
    digit = number % 10
    print("{:d}".format(digit), end='')
    return digit
