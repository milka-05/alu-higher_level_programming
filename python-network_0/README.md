# Python - Network #0

This directory contains tasks for learning HTTP requests and network communication.

## Task 0: Body size

**File:** `0-body_size.sh`

**Description:**
A Bash script that accepts a URL as an argument, sends a request using curl, and displays the size of the response body in bytes.

**Requirements:**
- Accept a URL as a command-line argument.
- Use curl to send the request.
- Display the response body size in bytes.

**Usage:**
./0-body_size.sh 0.0.0.0:5000

**Expected output:**
10

## Task 1: Body

**File:** `1-body.sh`

**Description:**
A Bash script that sends a GET request using curl and displays the response body only when the HTTP status code is 200.

**Usage:**
./1-body.sh 0.0.0.0:5000/route_1

**Expected output:**
Route 2

## Task 2: DELETE request

**File:** `2-delete.sh`

**Description:**
A Bash script that sends a DELETE request to a URL using curl and displays the response body.

**Usage:**
./2-delete.sh 0.0.0.0:5000/route_3

**Expected output:**
I'm a DELETE request

## Task 3: HTTP methods

**File:** `3-methods.sh`

**Description:**
A Bash script that sends an OPTIONS request using curl and displays all HTTP methods accepted by the server.

**Usage:**
./3-methods.sh 0.0.0.0:5000/route_4

**Expected output:**
OPTIONS, HEAD, PUT

## Task 4: Header

**File:** `4-header.sh`

**Description:**
A Bash script that sends a GET request using curl with a custom X-HolbertonSchool-User-Id header set to 98 and displays the response body.

**Usage:**
./4-header.sh 0.0.0.0:5000/route_5

**Expected output:**
Hello Holberton School!

## Task 5: POST parameters

**File:** `5-post_params.sh`

**Description:**
A Bash script that sends a POST request using curl with two parameters: email and subject. It displays the response body.

**Parameters:**
- email: test@gmail.com
- subject: I will always be here for PLD

**Usage:**
./5-post_params.sh 0.0.0.0:5000/route_6

**Expected output:**
POST params:
    email: test@gmail.com
    subject: I will always be here for PLD
