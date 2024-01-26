#!/usr/bin/python3
"""
Sends request to URL and display response body using responses module.

"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    try:
        response = requests.get(url)

        response.raise_for_status()

        print(response.text)

    except requests.exceptions.HTTPError as e:
        print(f"Error code: {response.status_code}")
