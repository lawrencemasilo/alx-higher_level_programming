#!/bin/bash
#takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -o temp_response.txt -w "%{http_code}" "$1" > /dev/null && [[ $(cat temp_response.txt) -eq 200 ]] && curl -s "$1"
