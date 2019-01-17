#!/usr/bin/python3
"""module for taking arguments and adds to a list, saves to file
"""


import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


def main():
    """contain main code in function
    """
    try:
        new_list = load_from_json_file('add_item.json')
    except:  # file didn't exist to read from
        new_list = []

    new_list.extend([sys.argv[i] for i in range(0, len(sys.argv)) if i != 0])
    try:
        save_to_json_file(new_list, 'add_item.json')
    except:
        pass

main()
