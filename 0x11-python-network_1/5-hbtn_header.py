#!/usr/bin/python3
"""This module fetches a URL"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    url_r = requests.get(url, auth=('user', 'pass'))
    x_request_id = url_r.headers['X-Request-Id']
    print(x_request_id)
