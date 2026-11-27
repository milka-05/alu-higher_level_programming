#!/bin/bash
# Send a request to a URL and display the response body size in bytes
curl -s "$1" | wc -c
