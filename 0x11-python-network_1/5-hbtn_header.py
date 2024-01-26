#!/usr/bin/python3
"""
Fetches data from the URL https://alx-intranet.hbtn.io/status using
requests module and display value of X-Request-Id header

"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    response = requests.get(url)

    header = response.headers.get('X-Request-Id')

    if header:
        print(header)
