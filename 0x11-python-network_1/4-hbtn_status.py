#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
using: package=requests
"""
if __name__ == '__main__':
    import requests
    req = requests.get('https://alx-intranet.hbtn.io/status')
    msg = req.text
    print("Body response:")
    print("\t- type: {}".format(type(msg)))
    print("\t- content: {}".format(msg))
