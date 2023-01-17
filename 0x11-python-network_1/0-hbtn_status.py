#!/usr/bin/python3
''' Fetches https://alx-intranet.hbtn.io/status, with urllib.
'''
from urllib import request

url = 'https://alx-intranet.hbtn.io/status'

with request.urlopen(url) as response:
    content = response.read()

    # Parse out the charset from `Content-Type` response header
    contentType = response.getheader('Content-Type')
    typeList = contentType.split(";")
    typeList = [x.strip() for x in typeList]
    for x in typeList:
        if x.startswith('charset'):
            charset = x.split("=")[1]

    # Display formated output
    print('Body response:')
    print(f'\t- type: {type(content)}')
    print(f'\t- content: {content}')
    print(f'\t- {charset} content: OK')
