#!/bin/bash
# Send a GET request and display the body only for HTTP 200 responses
body_file=$(mktemp) && { status=$(curl -sL -o "$body_file" -w '%{http_code}' "$1"); [ "$status" = "200" ] && cat "$body_file"; rm -f "$body_file"; }
