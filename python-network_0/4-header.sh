#!/bin/bash
# Send a GET request with a custom user ID header and display the response body
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
