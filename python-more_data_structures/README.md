# Python - More Data Structures: Set, Dictionary

This directory contains the tasks of the `alu-higher_level_programming` project about sets, dictionaries and more data structures.

## Tasks

### 0. Squared simple
**File:** `0-square_matrix_simple.py`

A function `def square_matrix_simple(matrix=[]):` that computes the square value of all integers of a matrix and returns a new matrix of the same size. The initial matrix is not modified, and no module is imported.

#### Usage

```bash
$ cat 0-main.py
#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

$ ./0-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
