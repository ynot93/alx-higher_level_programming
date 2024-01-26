#!/usr/bin/python3
"""
Fetches data from the URL https://alx-intranet.hbtn.io/status

"""
import urllib.request

if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        content = response.read()
        html = content.decode('utf-8')

    print("Body response:")
    print(f"\t- type : {type(content)}")
    print(f"\t- content : {content}")
    print(f"\t- utf8 content : {html}")
