#!/usr/bin/python3
"""This module fetches a URL"""
import requests

if __name__ == "__main__":
    url = requests.get(
            'https://alx-intranet.hbtn.io/status',
            auth=('user', 'pass')
            )

    print('Body response:')
    print(f'\t- type: {type(str(url.status_code))}')
    print(f'\t- content: {url.text}')
