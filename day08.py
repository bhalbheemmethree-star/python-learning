# ==========================================================
# PYTHON DAY 8
# STRING METHODS
# ==========================================================


# ==========================================================
# WHAT ARE STRING METHODS?
# ==========================================================

# String methods are built-in functions used to perform
# different operations on strings.

name = "python"

print(name.upper())

# Output

# PYTHON


# ==========================================================
# upper()
# ==========================================================

name = "python"

print(name.upper())

# Output

# PYTHON

# upper() converts all letters to uppercase.


# ==========================================================
# lower()
# ==========================================================

name = "PYTHON"

print(name.lower())

# Output

# python

# lower() converts all letters to lowercase.


# ==========================================================
# capitalize()
# ==========================================================

name = "python"

print(name.capitalize())

# Output

# Python

# capitalize() makes the first character uppercase
# and the remaining characters lowercase.


# ==========================================================
# title()
# ==========================================================

text = "python backend development"

print(text.title())

# Output

# Python Backend Development

# title() makes the first character of each word uppercase.


# ==========================================================
# swapcase()
# ==========================================================

text = "Python"

print(text.swapcase())

# Output

# pYTHON

# swapcase() changes uppercase letters to lowercase
# and lowercase letters to uppercase.


# ==========================================================
# strip()
# ==========================================================

text = "   Python   "

print(text.strip())

# Output

# Python

# strip() removes spaces from the beginning and end.


# ==========================================================
# lstrip()
# ==========================================================

text = "   Python"

print(text.lstrip())

# Output

# Python

# lstrip() removes spaces from the left side.


# ==========================================================
# rstrip()
# ==========================================================

text = "Python   "

print(text.rstrip())

# Output

# Python

# rstrip() removes spaces from the right side.


# ==========================================================
# replace()
# ==========================================================

text = "I like Java"

print(text.replace("Java", "Python"))

# Output

# I like Python

# replace() replaces one part of a string with another.


# ==========================================================
# split()
# ==========================================================

text = "Python Java C++"

result = text.split()

print(result)

# Output

# ['Python', 'Java', 'C++']

# split() divides a string into parts
# and returns them as a list.


# ==========================================================
# split() WITH SEPARATOR
# ==========================================================

text = "apple,banana,mango"

result = text.split(",")

print(result)

# Output

# ['apple', 'banana', 'mango']


# ==========================================================
# join()
# ==========================================================

words = ["Python", "is", "easy"]

result = " ".join(words)

print(result)

# Output

# Python is easy

# join() joins elements together using the given separator.


# ==========================================================
# find()
# ==========================================================

text = "I love Python"

print(text.find("Python"))

# Output

# 7

# find() returns the index of the first occurrence
# of the given substring.

# If it is not found, it returns -1.


# ==========================================================
# count()
# ==========================================================

text = "banana"

print(text.count("a"))

# Output

# 3

# count() returns the number of occurrences
# of a character or substring.


# ==========================================================
# startswith()
# ==========================================================

text = "Python Programming"

print(text.startswith("Python"))

# Output

# True

# startswith() checks whether a string starts
# with the specified value.


# ==========================================================
# endswith()
# ==========================================================

text = "Python Programming"

print(text.endswith("Programming"))

# Output

# True

# endswith() checks whether a string ends
# with the specified value.


# ==========================================================
# isalpha()
# ==========================================================

text = "Python"

print(text.isalpha())

# Output

# True

# isalpha() returns True if all characters are letters.


# ==========================================================
# isdigit()
# ==========================================================

text = "12345"

print(text.isdigit())

# Output

# True

# isdigit() returns True if all characters are digits.


# ==========================================================
# isalnum()
# ==========================================================

text = "Python123"

print(text.isalnum())

# Output

# True

# isalnum() returns True if all characters
# are letters or numbers.


# ==========================================================
# isspace()
# ==========================================================

text = "   "

print(text.isspace())

# Output

# True

# isspace() returns True if all characters are whitespace.


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# upper()      -> Converts to uppercase

# lower()      -> Converts to lowercase

# capitalize() -> Capitalizes the first character

# title()      -> Capitalizes the first character of each word

# swapcase()   -> Swaps uppercase and lowercase

# strip()      -> Removes spaces from both sides

# lstrip()     -> Removes spaces from left

# rstrip()     -> Removes spaces from right

# replace()    -> Replaces text

# split()      -> Splits string into a list

# join()       -> Joins elements into a string

# find()       -> Finds the first occurrence

# count()      -> Counts occurrences

# startswith() -> Checks the beginning

# endswith()   -> Checks the ending

# isalpha()    -> Checks whether all characters are letters

# isdigit()    -> Checks whether all characters are digits

# isalnum()    -> Checks whether all characters are
#                 letters or numbers

# isspace()    -> Checks whether all characters are spaces


# ==========================================================
# IMPORTANT
# ==========================================================

text = "python"

new_text = text.upper()

print(text)
print(new_text)

# Output

# python
# PYTHON

# String methods do not change the original string.
# They return a new string because strings are immutable.
