#!/usr/bin/python3
"""this program/module is used for modifying the heap of a program
    currently running
"""


import sys


def modify_heap():
    if len(sys.argv) != 4:
        print("Usage error: {} pid search_string replace_string".\
                format(sys.argv[0]))
    pid_dir = '/proc/' + sys.argv[1]
    with open(pid_dir + '/maps', 'r') as map_file:
        map_lines = map_file.readlines()
        for line in map_lines:
            if "[heap]" in line:
                heap_data = line.split()
                x_range = heap_data[0].split('-')
                if 'r' not in heap_data[1] or 'w' not in heap_data[1]:
                    print("read or write permissions not availble")
                    exit(1)
                with open(pid_dir + '/mem', 'rb+') as mem_file:
                    mem_file.seek(int(x_range[0], 16))
                    # read all bytes of heap
                    heap = mem_file.read(int(x_range[1], 16) -\
                                        int(x_range[0], 16))
                    builder = ""
                    for byte in heap:
                        if byte != 0:
                            builder += chr(byte)
                    print(builder)


modify_heap()
