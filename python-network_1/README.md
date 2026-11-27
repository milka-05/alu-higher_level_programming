
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
