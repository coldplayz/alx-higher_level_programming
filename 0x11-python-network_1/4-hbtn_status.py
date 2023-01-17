#!/usr/bin/python3
'''
Fetches https://alx-intranet.hbtn.io/status using Requests package.
'''
import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'

    # Get the Response object
    response = requests.get(url)

    print('Body response:')
    print(f'\t- type: {type(response.text)}')
    print(f'\t- content: {response.text}')
