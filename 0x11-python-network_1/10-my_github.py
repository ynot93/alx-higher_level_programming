#!/usr/bin/python3
"""
Takes in my GitHub credentials and sends GET request to the GitHub API
to display my id.

"""
import requests
import sys

if __name__ == '__main__':
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]

    credentials = (username, password)
    auth = requests.auth.HTTPBasicAuth(*credentials)

    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()

        result = response.json()
        print(result)
        print(result.get('id'))

    except requests.exceptions.HTTPError:
        print("None")
