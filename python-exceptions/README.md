# Python - Exceptions

This directory contains the tasks of the `alu-higher_level_programming` project about exceptions in Python.

## Tasks

### 0. Safe list printing
**File:** `0-safe_print_list.py`

A function `def safe_print_list(my_list=[], x=0):` that prints `x` elements of a list on the same line, followed by a new line, and returns the real number of elements printed. `x` can be bigger than the length of the list. It uses `try`/`except`, no module is imported, and `len()` is not used.

#### Usage

```bash
$ ./0-main.py
12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5
```

### 1. Integer printing
**File:** `1-safe_print_integer.py`

A function `def safe_print_integer(value):` that prints an integer with `"{:d}".format()`, followed by a new line. It returns `True` if `value` was correctly printed (it is an integer), otherwise `False`. It uses `try`/`except`, no module is imported, and `type()` is not used.

#### Usage

```bash
$ ./1-main.py
89
-89
School is not an integer
```
