#!/usr/bin/python3
"""script for testing status of web pages
"""
import requests
import sys
url = sys.argv[1]
with requests.get(url) as response:
    meta = response.headers
    try:
        print(meta['X-Request-Id'])
    except:
        pass
