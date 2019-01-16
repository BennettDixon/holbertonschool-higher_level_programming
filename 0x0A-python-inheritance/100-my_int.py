#!/usr/bin/python3


class MyInt(int):
    """inversed int, overriding operator methods / comparison methods
    """

    def __eq__(self, other):
        return (int(self) != other)

    def __ne__(self, other):
        return (int(self) == other)
