#!/usr/bin/python3
"""This module fetches a URL"""
import requests
import sys

if __name__ == "__main__":
    url = requests.get(
            f'{sys.argv[1]}',
            auth=('user', 'pass')
            )

    print(url.headers['X-Request-Id'])
