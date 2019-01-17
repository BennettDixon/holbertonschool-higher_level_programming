#!/usr/bin/python3
"""module for use in log debugging
"""


import sys


class DebugLog:
    """class for use in debugging stdin logs
    """
    def __init__(self):
        self.lines = []
        self.total_size = 0
        self.codes_200 = 0
        self.codes_401 = 0
        self.codes_403 = 0
        self.codes_404 = 0
        self.codes_405 = 0
        self.codes_500 = 0
        self.__current_line = 0

    def __str__(self):
        string = "File size: " + str(self.total_size) + '\n'
        string += "200: " + str(self.codes_200) + '\n'
        string += "401: " + str(self.codes_401) + '\n'
        string += "403: " + str(self.codes_403) + '\n'
        string += "404: " + str(self.codes_404) + '\n'
        string += "405: " + str(self.codes_405) + '\n'
        string += "500: " + str(self.codes_500)
        return string

    def update(self, iteration_n):
        """updates current response numbers
            with new set of lines
        """
        for i in range(self.__current_line, self.__current_line + iteration_n):
            if "200" in self.lines[i]:
                self.codes_200 += 1
            elif "401" in self.lines[i]:
                self.codes_401 += 1
            elif "403" in self.lines[i]:
                self.codes_403 += 1
            elif "404" in self.lines[i]:
                self.codes_404 += 1
            elif "405" in self.lines[i]:
                self.codes_405 += 1
            elif "500" in self.lines[i]:
                self.codes_500 += 1
            words = line.split(' ')
            self.total_size += int(words[-1])
            self.__current_line += 1


log = DebugLog()
lines = []
line = sys.stdin.readline()
while line != "":
    log.lines.append(line)
    if len(log.lines) % 10 == 0:
        log.update(10)
        print(log)
    line = sys.stdin.readline()
