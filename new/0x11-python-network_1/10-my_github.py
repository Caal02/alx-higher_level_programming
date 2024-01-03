#!/usr/bin/python3
"""
Takes your Github credentials and uses the GitHub API
to dispaly your ID.
using: package requests and sys
1st arg= username & 2nd arg= password
"""

import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    respo = requests.get(url, auth=(argv[1], argv[2]))
    try:
        print(respo.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
