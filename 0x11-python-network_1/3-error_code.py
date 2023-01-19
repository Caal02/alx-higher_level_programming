#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL & displays the body of the
response decoded in utf-8)
using: packages urllib and sys ,manage urllib.error.HTTPError exceptions
"""
if __name__ == "__main__":
    import urllib.error as error
    import urllib.request as request
    from sys import argv
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as url:
            print(url.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
