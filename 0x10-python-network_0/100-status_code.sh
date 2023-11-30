#!/bin/bash
#sends a request to a URL passed as an argument, and displays only the status code of the response
curl -s -o temp_response.txt -w "%{http_code}\n" "$1" > /dev/null ; cat temp_response.txt ; rm temp_response.txt
