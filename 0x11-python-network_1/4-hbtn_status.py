#!/usr/bin/python3
"""script for testing status of web pages
"""
import requests
url = "https://intranet.hbtn.io/status"
with requests.get(url) as response:
    content = response.text
    print_str = '''Body response:
\t- type: {}
\t- content: {}'''.format(type(content), content)
    print(print_str)
