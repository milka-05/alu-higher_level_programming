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

### 2. Print a list of integers
**File:** `2-safe_print_list_integers.py`

A function `def safe_print_list_integers(my_list=[], x=0):` that prints the first `x` elements of a list, only integers, on the same line followed by a new line. Other types are silently skipped. It returns the real number of integers printed. If `x` is bigger than the length of the list, an `IndexError` is expected to occur. It uses `try`/`except` and `"{:d}".format()`, no module is imported, and `len()` is not used.

#### Usage

```bash
$ ./2-main.py
12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
  File "./2-main.py", line 14, in <module>
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
  File "//2-safe_print_list_integers.py", line 7, in safe_print_list_integers
    print("{:d}".format(my_list[i]), end="")
IndexError: list index out of range
```

### 3. Safe integer division
**File:** `3-safe_print_division.py`

A function `def safe_print_division(a, b):` that divides 2 integers and prints the result in the `finally:` section, preceded by `Inside result:`. It returns the value of the division, otherwise `None`. It uses `try`/`except`/`finally` and `"{}".format()`, and no module is imported.

#### Usage

```bash
$ ./3-main.py
Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None
```

### 4. Divide lists element by element
**File:** `4-list_division.py`

A function `def list_division(my_list_1, my_list_2, list_length):` that divides elements from two lists element by element and returns a new list containing the results. If division is unsuccessful, it stores 0. It handles ZeroDivisionError, TypeError, and IndexError using try/except/finally. It prints the appropriate error message for each exception and does not import any module.

#### Usage

```bash
$ ./4-main.py
[5.0, 2.0, 1.0]
--
division by 0
wrong type
out of range
[5.0, 0, 0, 2.0, 0]

### 5. Raise a type exception
**File:** `5-raise_exception.py`

A function `def raise_exception():` that deliberately raises a TypeError exception using the raise keyword. No module is imported.

#### Usage

```bash
$ ./5-main.py
Exception raised
