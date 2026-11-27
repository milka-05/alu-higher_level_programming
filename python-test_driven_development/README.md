# python-test_driven_development

Test-driven development in Python with doctest.

## Task 0: Integers addition

**Files:** `0-add_integer.py`, `tests/0-add_integer.txt`

**Description:**
A function `add_integer(a, b=98)` that adds two integers or floats and returns an integer. Floats are cast to integers first.

**Requirements:**
- Raise `TypeError` with `a must be an integer` or `b must be an integer` if an argument is not an integer or float.
- Do not import any module.
- Tests are written as a doctest file in `tests/`.

**Usage:**
python3 -m doctest -v ./tests/0-add_integer.txt

**Expected output:**
Every test passes, with 0 failed.

## Task 2: Matrix division

**Files:** `2-matrix_divided.py`, `tests/2-matrix_divided.txt`

**Description:**
A function `matrix_divided(matrix, div)` that divides all elements of a matrix by `div`, rounded to 2 decimal places, and returns a new matrix.

**Requirements:**
- `matrix` must be a list of lists of integers or floats, otherwise raise `TypeError`.
- Each row must have the same size, otherwise raise `TypeError`.
- `div` must be a number, otherwise raise `TypeError`.
- `div` can't be 0, otherwise raise `ZeroDivisionError`.
- Do not import any module.

**Usage:**
python3 -m doctest -v ./tests/2-matrix_divided.txt

**Expected output:**
Every test passes, with 0 failed.

## Task 3: Say my name

**Files:** `3-say_my_name.py`, `tests/3-say_my_name.txt`

**Description:**
A function `say_my_name(first_name, last_name="")` that prints `My name is <first name> <last name>`.

**Requirements:**
- `first_name` and `last_name` must be strings, otherwise raise `TypeError`.
- Do not import any module.
- Tests are written as a doctest file in `tests/`.

**Usage:**
python3 -m doctest -v ./tests/3-say_my_name.txt

**Expected output:**
Every test passes, with 0 failed.

## Task 4: Print square

**Files:** `4-print_square.py`, `tests/4-print_square.txt`

**Description:**
A function `print_square(size)` that prints a square of `size` x `size` with the character `#`.

**Requirements:**
- `size` must be an integer, otherwise raise `TypeError`.
- If `size` is less than 0, raise `ValueError`.
- If `size` is a float and is less than 0, raise `TypeError`.
- Do not import any module.

**Usage:**
python3 -m doctest -v ./tests/4-print_square.txt

**Expected output:**
Every test passes, with 0 failed.

## Task 5: Text indentation

**Files:** `5-text_indentation.py`, `tests/5-text_indentation.txt`

**Description:**
A function `text_indentation(text)` that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`.

**Requirements:**
- `text` must be a string, otherwise raise `TypeError`.
- There should be no space at the beginning or at the end of each printed line.
- Do not import any module.

**Usage:**
python3 -m doctest -v ./tests/5-text_indentation.txt

**Expected output:**
Every test passes, with 0 failed.
