# Python - Data Structures: Lists and Tuples

This directory contains Python exercises that introduce data structures, particularly lists and tuples.

## Learning Objectives

- Understand Python lists and how to use them.
- Access and modify list elements.
- Use loops to work with lists.
- Understand tuples and their properties.
- Apply Python functions to data structures.

## Tasks

### 0. Print a list of integers

**File:** `0-print_list_integer.py`

Write a function called `print_list_integer(my_list=[])` that prints all integers in a list, with one integer per line.

**Example:**

```python
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
```

**Expected output:**

```text
1
2
3
4
5
```


### 1. Retrieve an element

**File:** `1-element_at.py`

Write a function called `element_at(my_list, idx)` that retrieves an element from a list using its index.

- Return the element when the index is valid.
- Return `None` when the index is negative.
- Return `None` when the index is outside the list.

**Example:**

```python
my_list = [1, 2, 3, 4, 5]
element_at(my_list, 3)
```

**Expected result:**

```text
4
```


### 2. Replace an element in a list

**File:** `2-replace_in_list.py`

Write a function called `replace_in_list(my_list, idx, element)` that replaces an element at a specific position in a list.

- Replace the element if the index is valid.
- Return the original list without modification if the index is negative.
- Return the original list without modification if the index is outside the list.
- Do not import any modules.
- Do not use try/except.

**Example:**

```python
my_list = [1, 2, 3, 4, 5]
replace_in_list(my_list, 3, 9)

### 3. Print a list in reverse order

**File:** `3-print_reversed_list_integer.py`

Write a function called `print_reversed_list_integer(my_list=[])` that prints all integers in a list in reverse order.

- Print one integer per line.
- Use `reversed()` to go through the list backwards.
- Use `str.format()` to print each integer.
- Do not import any modules.
- Do not cast integers into strings.

**Example:**

```python
my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

### 4. Replace an element without modifying the original list

**File:** `4-new_in_list.py`

Write a function called `new_in_list(my_list, idx, element)` that replaces an element at a specific position without changing the original list.

- Return a copy of the list.
- Replace the element if the index is valid.
- Return an unchanged copy if the index is negative.
- Return an unchanged copy if the index is outside the list.
- Do not import any modules.
- Do not use try/except.

**Example:**

```python
my_list = [1, 2, 3, 4, 5]
new_in_list(my_list, 3, 9)

### 5. Remove characters c and C from a string

**File:** `5-no_c.py`

Write a function called `no_c(my_string)` that returns a new string without lowercase `c` or uppercase `C`.

- Check each character in the original string.
- Keep every character except `c` and `C`.
- Do not import any modules.
- Do not use `str.replace()`.

**Example:**

```python
no_c("Best School")
no_c("Chicago")
no_c("C is fun!")
