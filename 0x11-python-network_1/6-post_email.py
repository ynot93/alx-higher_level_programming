#!/usr/bin/python3
"""
Sends Email as POST request and display response body using requests module.

"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}

    response = requests.post(url, data)
    print(response.text)
