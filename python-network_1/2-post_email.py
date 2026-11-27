#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

email = {"email": sys.argv[2]}
data = urllib.parse.urlencode(email).encode("utf-8")
request = urllib.request.Request(sys.argv[1], data=data)

with urllib.request.urlopen(request) as response:
    print(response.read().decode("utf-8"))
