#!/usr/bin/python3
"""This module fetches a URL"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    content = response.read()

print('Body response:')
print(f'    - type: {type(content)}')
print(f'    - content: {content}')
print(f'    - utf8 content: {content.decode("utf-8")}')
