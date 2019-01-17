#!/usr/bin/python3
"""this program/module is used for modifying the heap of a program
    currently running
"""


import sys


def modify_heap():
    if len(sys.argv) != 4:
        print("Usage error: {} pid search_string replace_string" +
              str(sys.argv[0]))
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

                heap_start = int(x_range[0], 16)
                heap_end = int(x_range[1], 16)

                with open(pid_dir + '/mem', 'rb+') as mem_file:
                    mem_file.seek(heap_start)
                    # read all bytes of heap
                    heap = mem_file.read(heap_end - heap_start)
                    builder = ""
                    for i, byte in enumerate(heap):
                        if chr(byte) in sys.argv[2]:
                            if builder == "":
                                str_offset = i
                            builder += chr(byte)
                            if builder == sys.argv[2]:
                                break
                        elif byte != 0:  # found semi-matching garbage
                            builder = ""  # reset
                    if builder != sys.argv[2]:
                        print("couldn't find search string in heap")
                        print(builder)
                        exit(1)
                    mem_file.seek(heap_start + str_offset)
                    mem_file.write(bytes(sys.argv[3] + '\0', "ASCII"))
modify_heap()
