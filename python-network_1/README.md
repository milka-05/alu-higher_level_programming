
## Task 0: What's my status?

**File:** `0-hbtn_status.py`

**Description:**
A Python script that fetches a URL using urllib and displays the response body in bytes and UTF-8 format.

**Requirements:**
- Use the urllib package.
- Use a with statement.
- Display the response type, content in bytes, and decoded UTF-8 content.

**Usage:**
./0-hbtn_status.py

**Expected output:**
Body response:
    - type: <class 'bytes'>
    - content: b'OK'
    - utf8 content: OK

## Task 1: Response header value

**File:** `1-hbtn_header.py`

**Description:**
A Python script that sends a request to a URL and displays the value of the `X-Request-Id` response header.

**Requirements:**
- Use `urllib` and `sys`.
- Do not import other packages.
- Use a `with` statement.
- Get the URL from the command-line arguments.
- Display the `X-Request-Id` header value.

**Usage:**
./1-hbtn_header.py https://intranet.hbtn.io

**Expected output:**
A unique request ID, for example:
6593e1f5-1b4b-4c9f-9c0e-72ab525b850f

## Task 2: POST an email

**File:** `2-post_email.py`

**Description:**
A Python script that sends an email address to a URL using a POST request and displays the response body decoded in UTF-8.

**Requirements:**
- Use `urllib` and `sys`.
- Do not import packages other than `urllib` and `sys`.
- Send the email using the `email` parameter.
- Use a `with` statement.
- Decode the response body using UTF-8.

**Usage:**
./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com

**Expected output:**
Your email is: hr@holbertonschool.com

## Task 3: Error code

**File:** `3-error_code.py`

**Description:**
A Python script that sends a request to a URL, displays the response body decoded in UTF-8, and handles HTTP errors by displaying their status codes.

**Requirements:**
- Use `urllib` and `sys`.
- Do not import packages other than `urllib` and `sys`.
- Use a `with` statement.
- Catch `urllib.error.HTTPError`.
- Display `Error code: ` followed by the HTTP status code when an HTTP error occurs.

**Usage:**
./3-error_code.py http://0.0.0.0:5000

**Expected output for a successful request:**
Index

**Expected output for an HTTP error:**
Error code: 401

## Task 4: Status with requests

**File:** `4-hbtn_status.py`

**Description:**
A Python script that fetches `https://intranet.hbtn.io/status` using the `requests` package and displays the response body.

**Requirements:**
- Use the `requests` package.
- Do not import packages other than `requests`.
- Display the body with a tabulation before `- `.

**Usage:**
./4-hbtn_status.py

**Expected output:**
Body response:
    - type: <class 'str'>
    - content: OK

## Task 5: Response header value with requests

**File:** `5-hbtn_header.py`

**Description:**
A Python script that sends a request to a URL using the `requests` package and displays the value of the `X-Request-Id` response header.

**Requirements:**
- Use `requests` and `sys`.
- Do not import other packages.
- Get the URL from the command-line arguments.
- Display the `X-Request-Id` header value, which is different for each request.

**Usage:**
./5-hbtn_header.py https://intranet.hbtn.io

**Expected output:**
A unique request ID, for example:
5e52e160-c822-4669-8b3a-8b3bbca7b090
