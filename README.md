# Python Basics

*by Suyash Lakhotia for IEEE NTU Student Branch*

***Disclaimer*** *-* *This document is only meant to serve as a reference for the attendees of the workshop. It does not cover all the concepts or implementation details discussed during the actual workshop.*

### What is Python?

- Python is a general purpose **programming language**. Other examples include Java, C, C++ etc.
- It is known for its remarkable power coupled with readable *syntax*.
    - The *syntax* of a programming language is the set of rules that defines the combinations of symbols that are considered to be correctly structured pieces of code. Think: Spelling & Grammar.
- It is one of the easiest programming languages to learn but is also one of the most powerful languages, used heavily in machine learning and data science.
- Python code is executed line-by-line in a sequential fashion.

## Basic Syntax

```python
# Basic Python Example

print("This is an example of Python code.")

a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))
print("The sum of a & b is: " + (a + b))  # print the sum of a & b
```

**Statement:** Each line of code in a Python program is called a statement. Python interprets statements and runs them one by one.

**Comments:** The `#` symbol indicates a comment and anything after `#` is ignored by the computer. Comments provide information to improve code readability.

**Built-in Functions:** Python comes with many built-in functions like `print()` & `input()` to help you in writing your code.

## Variables

#### What are variables?

Recall variables from algebra — `x = 5`. In programming, variables are used to store data to make it easier to refer to them. The value referred to by a variable can be updated as you execute the program using the *assignment operator* i.e. `=`.

```python
a = 3       # simple assignment
a = a + 1   # RHS is evaluated first
print(a)    # 4
```

There are four basic data types in Python:

1.  **Integer -** Whole numbers. E.g. `1`, `123`, `89`
2.  **Float -** Floating decimal point numbers. E.g. `1.3`, `82.4`, `3.14159…`
3.  **String -** Sequence of characters. E.g. `a`, `abc`, `abc def`
4.  **Boolean -** Two possible values — `True` or `False`.

```python
a = 5
b = 4.3
c = "Hello, world"
d = True
```

It is possible to convert a variable from one type to another if the conversion is compatible. For example, converting `"123"` (string) to `123` (integer) is possible.

```python
strA = "123"
intA = int(strA)      # 123
floatA = float(strA)  # 123.0
```

#### Printing Variables

In Python, we can print text onto the *console* using the `print()` function.

```python
print("Hello, world")

a = 5
print(a)
print("The value of 'a' is: " + a)
```

#### Arithmetic Operations

Variables can be used to perform simple arithmetic operations. For example:

```python
a = 4
b = 5
c = a + b	# addition
d = a - b	# subtraction
e = a * b	# multiplication
f = a / b	# division
g = a % b	# modulus (remainder)
```

#### Strings

Strings represent a sequence of one or more characters. Each character can be accessed separately using a zero-based index.

```
H  e  l  l  o
0  1  2  3  4
```

```python
s = "Hello"
print(s[1])
print(len(s))
print(s + ", world")
```

Python comes with a lot of useful built-in *methods* for strings.

```python
s.lower()                   # returns lowercase version of string
s.upper()                   # returns uppercase version of string
s.find("abc")               # searches the string for "abc" and returns the first index where it begins or -1
s.replace("old", "new")     # returns a string with all occurrences of "old" replaced with "new"
```

If you want to access a part of a string, Python allows you to *slice* the string using the start and end indices.

```python
s = "hello"
print(s[1:4])   # "ell"
print(s[1:])    # "ello"
print(s[:3])    # "hel"
print(s[:])     # "hello"
```

#### Lists

Instead of variables holding individual values, it is also possible to create a list of values in Python. Each item in the list is called an *element* and can be accessed individually using a zero-based index.

```python
listOfNums = [1, 2, 3, 4, 5]
print(listOfNums)
print(listOfNums[1])
print(len(listOfNums))
```

#### Dictionaries

Dictionaries in Python allow you to store key-value pairs. Keys are unique within a dictionary while values may be repeated. For example, a dictionary of names (keys) and ages (values). Because the keys are unique, they are used as the index of the dictionary to access the values.

```python
phoneBook = {"Bob" : 21, "Jake" : 24, "John" : 23}
print(phoneBook["Bob"])   # 21
print(phoneBook["Jake"])  # 24

phoneBook["Jane"] = 23
print(phoneBook)  # {"Bob" : 21, "Jake" : 24, "John" : 23, "Jane" : 23}

phoneBook["Bob"] = 24
print(phoneBook)  # {"Bob" : 24, "Jake" : 24, "John" : 23, "Jane" : 23}

print(phoneBook.keys())  # ["Bob", "Jake", "John", "Jane"]
```

