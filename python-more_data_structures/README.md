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

### 1. Search and replace
**File:** `1-search_replace.py`

A function `def search_replace(my_list, search, replace):` that replaces all occurrences of an element by another in a new list. The initial list is not modified, and no module is imported.

#### Usage

```bash
$ ./1-main.py
[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
```

### 2. Uniq addition
**File:** `2-uniq_add.py`

A function `def uniq_add(my_list=[]):` that adds all unique integers in a list (only once for each integer). No module is imported.

#### Usage

```bash
$ ./2-main.py
Result: 15
```

### 3. Common elements
**File:** `3-common_elements.py`

A function `def common_elements(set_1, set_2):` that returns a set of common elements in two sets. No module is imported.

#### Usage

```bash
$ ./3-main.py
['C']
```

### 4. Only differents
**File:** `4-only_diff_elements.py`

A function `def only_diff_elements(set_1, set_2):` that returns a set of all elements present in only one set. No module is imported.

#### Usage

```bash
$ ./4-main.py
['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
```

### 5. Number of keys
**File:** `5-number_keys.py`

A function `def number_keys(a_dictionary):` that returns the number of keys in a dictionary. No module is imported.

#### Usage

```bash
$ ./5-main.py
Number of keys: 3
```

### 6. Print sorted dictionary
**File:** `6-print_sorted_dictionary.py`

A function `def print_sorted_dictionary(a_dictionary):` that prints a dictionary by ordered keys. Only first-level keys are sorted, and no module is imported.

#### Usage

```bash
$ ./6-main.py
Number: 89
ids: [1, 2, 3]
language: C
track: Low level
```

### 7. Update dictionary
**File:** `7-update_dictionary.py`

A function `def update_dictionary(a_dictionary, key, value):` that replaces or adds a key/value in a dictionary. If the key exists the value is replaced, otherwise the key is created. No module is imported.

#### Usage

```bash
$ ./7-main.py
language: Python
number: 89
track: Low level
--
language: Python
number: 89
track: Low level
--
--
city: San Francisco
language: Python
number: 89
track: Low level
--
city: San Francisco
language: Python
number: 89
track: Low level
```

### 8. Delete by key
**File:** `8-simple_delete.py`

A function `def simple_delete(a_dictionary, key=""):` that deletes a key in a dictionary. If the key doesn't exist, the dictionary won't change. No module is imported.

#### Usage

```bash
$ ./8-main.py
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
--
--
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
```

### 9. Multiply by 2
**File:** `9-multiply_by_2.py`

A function `def multiply_by_2(a_dictionary):` that returns a new dictionary with all values multiplied by 2. All values are assumed to be integers, and no module is imported.

#### Usage

```bash
$ ./9-main.py
Alex: 8
Bob: 14
John: 12
Mike: 14
Molly: 16
--
Alex: 16
Bob: 28
John: 24
Mike: 28
Molly: 32
```

### 10. Best score
**File:** `10-best_score.py`

A function `def best_score(a_dictionary):` that returns a key with the biggest integer value. If no score is found, it returns `None`. No module is imported.

#### Usage

```bash
$ ./10-main.py
Best score: Molly
Best score: None
```

### 11. Multiply list map
**File:** `11-multiply_list_map.py`

A function `def multiply_list_map(my_list=[], number=0):` that returns a new list with all values multiplied by a number, using `map` and no loops. The initial list is not modified, no module is imported, and the file is at most 3 lines long.

#### Usage

```bash
$ ./11-main.py
[4, 8, 12, 16, 24]
[1, 2, 3, 4, 6]
```
