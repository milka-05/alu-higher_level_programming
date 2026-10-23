# Python - Hello, World

This directory contains the first tasks of the `alu-higher_level_programming` project.

## Tasks

### 0. Run Python file
**File:** `0-run`

A Bash script that runs the Python file whose name is stored in the environment variable `$PYFILE`.

#### Usage

```bash
$ cat main.py
#!/usr/bin/python3
print("Best School")

$ export PYFILE=main.py
$ ./0-run
Best School
```

## Requirements
- Ubuntu with Python 3 installed
- Scripts start with a shebang and are executable
- All files end with a new line

### 1. Run inline
**File:** `1-run_inline`

A Bash script that runs the Python code stored in the environment variable `$PYCODE`.

#### Usage

```bash
$ export PYCODE='print(f"Best School: {88+10}")'
$ ./1-run_inline
Best School: 98
```

### 2. Print a sentence
**File:** `2-print.py`

A Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line, using the `print` function.

#### Usage

```bash
$ ./2-print.py
"Programming is like building a multilingual puzzle
```

### 3. Print number
**File:** `3-print_number.py`

A Python script that prints the integer stored in the variable `number`, followed by `Battery street` and a new line, using an f-string and without casting `number` to a string.

#### Usage

```bash
$ ./3-print_number.py
98 Battery street
```

### 4. Print float
**File:** `4-print_float.py`

A Python script that prints the float stored in the variable `number` with a precision of 2 digits, using an f-string and without casting `number` to a string.

#### Usage

```bash
$ ./4-print_float.py
Float: 3.14
```
