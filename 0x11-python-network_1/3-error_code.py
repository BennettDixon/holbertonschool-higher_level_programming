#!/usr/bin/python3
"""script for testing status of web pages
"""
if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as resp:
            print(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
