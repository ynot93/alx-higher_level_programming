#!/usr/bin/python3
"""
Takes in a letter and sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.

"""
import requests
import sys

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    data = {'q': q}

    try:
        response = requests.post(url, data)
        response.raise_for_status()

        result = response.json()

        if result:
            print(f"[{result.get('id')}] {result.get('name')}")
        else:
            print("No result")
    except requests.exceptions.HTTPError:
            print("Not a valid JSON")
