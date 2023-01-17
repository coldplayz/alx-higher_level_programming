#!/usr/bin/python3
''' Fetches https://alx-intranet.hbtn.io/status, with urllib.
'''
from urllib import request

url = 'https://alx-intranet.hbtn.io/status'

with request.urlopen(url) as response:
    html = response.read()
