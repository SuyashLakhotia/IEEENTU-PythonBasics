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

### What are variables?

Recall variables from algebra — `x = 5`. In programming, variables are used to store data temporarily to make it easier to refer to them. The value referred to by a variable can be updated as you execute the program using the *assignment operator* i.e. `=`.

```python
a = 3       # simple assignment
a = a + 1   # RHS is evaluated first
print(a)    # 4
```

There are four basic data types in Python:

1. **Integer -** Whole numbers. E.g. `1`, `123`, `89`
2. **Float -** Floating decimal point numbers. E.g. `1.3`, `82.4`, `3.14159…`
3. **String -** Sequence of characters. E.g. `a`, `abc`, `abc def`
4. **Boolean -** Two possible values — `True` or `False`.

```python
a = 5
b = 4.3
c = "Hello, world"
d = True
```

It is possible to convert a variable from one type to another if the conversion is compatible. For example, converting `"123"` (string) to `123` (integer) is possible but `"hello"` cannot be converted to an integer.

```python
strA = "123"
intA = int(strA)      # 123
floatA = float(strA)  # 123.0
```

### Printing Variables

In Python, we can print text onto the *console* using the `print()` function.

```python
print("Hello, world")

a = 5
print(a)
print("The value of 'a' is: " + a)
```

### Getting User Input

In Python, we can get input from the user and store this in variables using the `input()` function. The function prints whatever prompt is passed to it and waits for the user input. Once the `Enter` key is pressed, it stores the user input into the variable **as a string**.

```python
name = input("Enter your name: ")
print(name)

age = int(input("Enter your age: "))
print(age)
```

### Arithmetic Operations

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

### Strings

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

### Lists

Instead of variables holding individual values, it is also possible to create a list of values in Python. Each item in the list is called an *element* and can be accessed individually using a zero-based index.

```python
listOfNums = [1, 2, 3, 4, 5]
print(listOfNums)
print(listOfNums[1])
print(len(listOfNums))
```

### Dictionaries

Dictionaries in Python allow you to store key-value pairs. Keys are unique within a dictionary while values may be repeated. For example, a dictionary of names (keys) and ages (values). Because the keys are unique, they are used as the index of the dictionary to access the values.

```python
ages = {"Bob" : 21, "Jake" : 24, "John" : 23}
print(ages["Bob"])   # 21
print(ages["Jake"])  # 24

ages["Jane"] = 23
print(ages)  # {"Bob" : 21, "Jake" : 24, "John" : 23, "Jane" : 23}

ages["Bob"] = 24
print(ages)  # {"Bob" : 24, "Jake" : 24, "John" : 23, "Jane" : 23}

print(ages.keys())  # ["Bob", "Jake", "John", "Jane"]
```

## Control Flow

While sequentially executing code can perform a lot of tasks for us, many tasks require some subtask to be repeated or selectively executed. For example, if we want to calculate the average age in a classroom:

```python
total = 0
numOfStudents = 0

studentAge = int(input("What's your age? "))
total = total + studentAge
numOfStudents = numOfStudents + 1

studentAge = int(input("What's your age? "))
total = total + studentAge
numOfStudents = numOfStudents + 1

studentAge = int(input("What's your age? "))
total = total + studentAge
numOfStudents = numOfStudents + 1

...

average = total / numOfStudents
```

Repeating the same lines of code is tedious and limits the reusability & maintainability of the code. For example, in the above code, if we just wanted to change the user prompt to `Enter your age:` instead, we would have to change many lines of code.

### if Statements

`if` statements are one of the most important control flow tools available in programming. They allow the program to dynamically choose which lines of code to execute depending on a particular condition.

```python
if <condition>:
    # Statements here are executed if condition is True
else:
    # Statements here are executed if condition is False
```

```python
if <conditionA>:
    # Statements here are executed if conditionA is True
elif <conditionB>:
    # Statements here are executed if conditionA is False and conditionB is True
else:
    # Statements here are executed if conditionA and conditionB are False
```

A colon marks the beginning of a *block* and statements within each *block* are indented so that they can be distinguished from each other.

#### Condition

Conditions are *boolean expressions* that return either `True` or `False`. They are made up of *relational operators* and *logical operators*.

##### Relational Operators

1. `==`: equals to
2. `!=`: not equals to
3. `<` : smaller than
4. `>` : greater than
5. `<=`: smaller than or equals to
6. `>=`: greater than or equals to

```python
if x == y:
    print("x & y are equal.")
else:
    print("x & y are not equal.")
```

##### Logical Operators

1. `boolExpr1 and boolExpr2`: Both expressions have to be `True` for the entire expression to be `True`
2. `boolExpr1 or boolExpr2`: Either one expression has to be `True` for the entire expression to be `True`
3. `not boolExpr`: Inverts the return value of the expression

```python
if (x == y) and (y == z):
    print("x, y & z are equal.")
```

### Loops

Loops in programming allow the same task to be executed repeatedly for a definite or indefinite number of times. They are made up of four main sections:

1. **Initialize:** Initialize the loop control variable.
2. **Test:** Continue the loop?
3. **Loop Body:** Task being repeated.
4. **Update:** Modify the loop control variable so that the next time we test, we *may* exit the loop.

There are two main kinds of loops:

1. **Counter Controlled:** The number of repetitions of the loop is known before the loop body starts executing.
2. **Sentinel Controlled:** The number of repetitions of the loop is unknown before the loop body starts executing.

#### while Loop

A `while` loop executes while the given condition is `True` (i.e. until the given condition is `False`).

```python
while <condition>:
    # Loop Body
```

For example, to print all the integers from 1 - 10:

```python
num = 1                 # Initialize
while num <= 10:        # Test
    print(num)          # Loop Body
    num = num + 1       # Update
```

An example of a sentinel controlled loop:

```python
answer = 5
guess = int(input("Guess a number from 1 - 10: "))
while guess != answer:
    guess = int(input("Wrong! Guess a number from 1 - 10: "))
print("Correct!")
```

#### for Loop

A `for` loop can be used to iterate through a list and perform tasks accordingly.

```python
for var in someList:
    # Loop Body
```

In every iteration of the loop, the `var` variable will be assigned the next value in the list. For example, the code below will print all the elements in the list in separate lines:

```python
numList = [2, 1, 4, 5, 3]
for num in numList:
    print(num)
```

A `for` loop can also be used to iterate through a dictionary:

```python
phoneBook = {"Bob" : "555-555", "Jake" : "555-556", "John" : "555-565", "Jane" : "555-655"}
for name in phoneBook.keys():
    print(name + " : " phoneBook[name])
```

Alternatively, a `for` loop can be used like a `while` loop with a definite number of repetitions using the `range()` function. The `range()` function returns a list of integers from 0 up till but not including the passed argument.

```python
for i in range(5):  # range(5) returns [0, 1, 2, 3, 4]
    print(i)
```

## Functions

Functions allow you to divide your code into chunks that do specific subtasks, which make your code more readable and reusable.

```python
# Define the function
def functionName():
    # Function Body

functionName()  # Call the function
```

### Parameters & Arguments

Functions can be defined with *parameters*, which are essentially variables that are set when the function is called using *arguments*. This allows functions to be reused with different data values.

```python
def sum(a, b):  # a & b are parameters
    c = a + b
    print(c)

sum(3, 2)       # 3 & 2 are arguments
sum(32, 65)     # 32 & 65 are arguments
```

### Return Values

Functions can also return values back to where the function was called so that the result can be further used.

```python
def sum(a, b):
    c = a + b
    return c

s = sum(a, b)   # s is set to the value of c from sum()
print(s)
```
