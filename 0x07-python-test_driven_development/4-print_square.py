#!/usr/bin/python3


def print_square(size):
    """
    prints a square of given size
    unit tests are located in tests/4-print_square.txt
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    elif size < 0:
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")

    size = int(size)  # if it was a float convert it
    i = 0

    for i in range(0, size):
        j = 0
        for j in range(0, size):
            print('#', end='')
        print()
