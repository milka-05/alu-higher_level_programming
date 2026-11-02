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

