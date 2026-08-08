# ==========================================================
# PYTHON - STRINGS
# ==========================================================

# ==========================================================
# STRING
# ==========================================================

# String:
# A string is a sequence of characters enclosed inside quotes.

name = "Bhalbheem"
college = 'KMIT'

print(name)
print(college)

# Python supports both single and double quotes.


# ==========================================================
# TYPES OF CHARACTERS IN A STRING
# ==========================================================

name = "Bhalbheem"
number = "12345"
special = "@#$%"
sentence = "Hello Python!"

# All of these are strings because they are enclosed in quotes.


# ==========================================================
# STRING WITH NUMBERS
# ==========================================================

x = "123"

print(x)
print(type(x))

# Output

# 123
# <class 'str'>

# "123" is a string.
# 123 is an integer.


# ==========================================================
# EMPTY STRING
# ==========================================================

name = ""

print(name)
print(type(name))

# Output

# <class 'str'>

# An empty string contains no characters,
# but its data type is still str.


# ==========================================================
# QUOTES INSIDE STRINGS
# ==========================================================

message = "I'm learning Python"

print(message)

message = 'He said "Hello"'

print(message)

# Different types of quotes can be used
# to include quotes inside a string.


# ==========================================================
# ESCAPE QUOTES
# ==========================================================

message = "He said \"Hello\""

print(message)

# \" allows a double quote to be used
# inside a double-quoted string.


# ==========================================================
# MULTILINE STRINGS
# ==========================================================

message = """Hello
I am learning Python
I want to become a backend developer"""

print(message)

# Triple quotes can be used for multiline strings.


# ==========================================================
# STRINGS ARE ORDERED
# ==========================================================

name = "Python"

# Characters are stored in a specific order.

# P y t h o n

# Indexing and slicing will be covered
# in separate topics.


# ==========================================================
# STRINGS ARE IMMUTABLE
# ==========================================================

name = "Python"

# name[0] = "J"   # Error

# Individual characters of an existing string
# cannot be changed directly.

# We can create a new string instead.

name = "Jython"


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# String → sequence of characters

# Strings can be created using:
# "double quotes"
# 'single quotes'
# """triple quotes"""
# '''triple quotes'''

# "123" → str
# 123   → int

# "" → empty string

# Strings are ordered.

# Strings are immutable.
