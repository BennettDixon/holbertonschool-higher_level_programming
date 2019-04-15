#!/usr/bin/python3
"""script for testing status of web pages
"""
import urllib.request
import urllib.error
import sys
url = sys.argv[1]
try:
    urllib.request.urlopen(url)
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
