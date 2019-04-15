#!/usr/bin/python3
"""script for testing status of web pages
"""
import urllib.request
import sys
url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    meta = response.info()
    for header in meta._headers:
        if header[0] == 'X-Request-Id':
            print(header[1])
