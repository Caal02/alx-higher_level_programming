#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status using
package urlib and with statment
"""
if __name__ == "__main__":
    import urllib.request as request
    with request.urlopen('https://alx-intranet.hbtn.io/status') as req:
        url = req.read()
        print('Body response:')
        print("\t- type: {}".format(type(url)))
        print("\t- content: {}".format(url))
        print("\t- utf8 content: {}".format(url.decode('utf-8')))
