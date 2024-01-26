#!/usr/bin/python3
"""
List last 10 commits of the user rails of repository rails.

"""
import requests
import sys

if __name__ == '__main__':
    owner = sys.argv[2]
    repo = sys.argv[1]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    try:
        response = requests.get(url)
        response.raise_for_status()

        result = response.json()[:10]

        for commit in result:
            sha = commit.get('sha')
            name = commit.get('commit').get('author').get('name')
            print(f"{sha}:  {name}")

    except requests.exceptions.HTTPError:
        print("None")
