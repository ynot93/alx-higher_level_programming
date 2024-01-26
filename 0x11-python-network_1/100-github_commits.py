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

    response = requests.get(url)

    result = response.json()[:10]

    for commit in result:
        sha = commit.get('sha')
        name = commit.get('commit').get('author').get('name')
        print(f"{sha}:  {name}")
