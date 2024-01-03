#!/usr/bin/python3
"""Write a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
using: variable q, package = requests and sys
If the response body is properly JSON formatted and not empty,
display the id and name
"""

import requests
from sys import argv

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": argv[1][0] if len(argv) > 1 else ""}
    response = requests.post(url, data=data)
    try:
        respo = response.json()
        if not respo:
            print("No result")
        else:
            print("[{}] {}".format(respo.get("id"), respo.get("name")))
    except ValueError:
        print("Not a valid JSON")
