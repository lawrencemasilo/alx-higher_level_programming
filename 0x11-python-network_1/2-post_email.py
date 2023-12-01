#!/usr/bin/python3
"""This module posts an email"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': f'{sys.argv[2]}'}
    data = urllib.parse.urlencode(email)
    data = data.encode('utf-8')

    url = urllib.request.Request(url, data)
    with urllib.request.urlopen(url) as response:
        email_data = response.read().decode('utf-8')

    print(email_data)
