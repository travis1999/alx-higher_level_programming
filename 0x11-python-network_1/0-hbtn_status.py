#!/usr/bin/python3
"""python script that fetches url"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as resp:
        html = resp.read()
        print("Body response:")
        print("\t- type: {:}".format(type(html)))
        print("\t- content: {:}".format(html))
        print("\t- utf8 content: {:}".format(html.decode('utf-8')))
