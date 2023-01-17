#!/usr/bin/python3
'''
Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
'''
import requests
from sys import argv

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    try:
        q = argv[1]
    except IndexError:
        q = ""

    # Get the Response object
    response = requests.post(url, data={'q': q})

    try:
        jsonList = response.json()
        if len(jsonList) == 0 or len(jsonList[0]) == 0:
            print('No result')
        else:
            dct = jsonList[0]
            for k, v in dct.items():
                print(f'[{k}] {v}')
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')
