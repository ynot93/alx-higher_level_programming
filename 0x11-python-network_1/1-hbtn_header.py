#!/usr/bin/python3
"""
Displays value of X-Request-Id found in the header of the response.

"""
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        header_content = response.getheader('X-Request-Id')
    if header_content:
        print(header_content)
