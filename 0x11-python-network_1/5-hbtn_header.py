#!/usr/bin/python3
"""script for testing status of web pages
"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    with requests.get(url) as response:
        meta = response.headers
        try:
            print(meta['X-Request-Id'])
        except:
            pass
