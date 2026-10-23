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
