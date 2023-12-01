#!/usr/bin/python3
"""This module fetches a URL"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    url_r = requests.get(url)

    print(url_r.headers['X-Request-Id'])
