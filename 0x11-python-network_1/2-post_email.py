#!/usr/bin/python3
'''
Takes in a URL and an email, sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response (decoded in utf-8)
'''
from urllib import request, parse
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    email = argv[2]

    # Get data in encoded form
    data = {'email': email}
    data = parse.urlencode(data).encode('ascii')

    # Form a Request object from the data
    req = request.Request(url, data)

    # Get response object
    with request.urlopen(req) as response:
        body = response.read().decode('utf8')
        print(body)
