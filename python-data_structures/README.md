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

### 6. Print a matrix of integers

**File:** `6-print_matrix_integer.py`

Write a function called `print_matrix_integer(matrix=[[]])` that prints a matrix of integers.

- Print each row on a separate line.
- Separate integers in each row with a space.
- Use `str.format()` to print integers.
- Do not cast integers into strings.
- Do not import any modules.

**Example:**

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_integer(matrix)

### 7. Add two tuples

**File:** `7-add_tuple.py`

Write a function called `add_tuple(tuple_a=(), tuple_b=())` that adds the first two elements of two tuples.

- Return a tuple containing exactly two integers.
- Add the first elements together.
- Add the second elements together.
- Use 0 when an element is missing.
- Ignore elements after the second position.
- Do not import any modules.

**Example:**

```python
tuple_a = (1, 89)
tuple_b = (88, 11)
add_tuple(tuple_a, tuple_b)

### 8. Multiple returns

**File:** `8-multiple_returns.py`

Write a function called `multiple_returns(sentence)` that returns a tuple containing the length of a string and its first character.

- Return the length of the string.
- Return the first character of the string.
- If the string is empty, return None as the first character.
- Do not import any modules.

**Example:**

```python
sentence = "At school, I learnt C!"
multiple_returns(sentence)

### 9. Find the biggest integer in a list

**File:** `9-max_integer.py`

Write a function called `max_integer(my_list=[])` that returns the biggest integer in a list.

- Return None if the list is empty.
- Use a loop to compare the integers.
- Do not use the built-in max() function.
- Do not import any modules.

**Example:**

```python
my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_integer(my_list)

### 10. Find multiples of 2 in a list

**File:** `10-divisible_by_2.py`

Write a function called `divisible_by_2(my_list=[])` that returns a new list of Boolean values.

- Return True if an integer is divisible by 2.
- Return False if an integer is not divisible by 2.
- The new list must have the same size as the original list.
- Do not import any modules.

**Example:**

```python
my_list = [0, 1, 2, 3, 4, 5, 6]
divisible_by_2(my_list)
