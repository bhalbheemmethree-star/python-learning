# ==========================================================
# PYTHON DAY 3
# VARIABLES & DATA TYPES
# ==========================================================

# ==========================================================
# VARIABLES
# ==========================================================

# Variable:
# A variable is a name used to store a value in memory.

name = "Bhalbheem"
age = 18
height = 180.5

print(name)
print(age)
print(height)

# Output

# Bhalbheem
# 18
# 180.5

# Python automatically decides the data type.
# This is called Dynamic Typing.


# ==========================================================
# VARIABLE NAMING RULES
# ==========================================================

# Valid Variables

student_name = "Python"
_marks = 95
age2 = 18

# Invalid Variables

# 2age = 18
# student-name = "Python"
# class = "Python"

# Rules

# Can contain:
# Letters
# Numbers
# Underscore (_)

# Cannot:
# Start with a number
# Contain spaces
# Use Python keywords


# ==========================================================
# DATA TYPES
# ==========================================================

# Integer

age = 18

# Float

height = 180.5

# String

name = "Bhalbheem"

# Boolean

is_student = True

# None

data = None

# Python Data Types

# int
# float
# str
# bool
# NoneType


# ==========================================================
# DYNAMIC TYPING
# ==========================================================

x = 10
print(type(x))

x = "Python"
print(type(x))

x = 3.14
print(type(x))

# Output

# <class 'int'>
# <class 'str'>
# <class 'float'>

# Python allows the same variable to store different data types.


# ==========================================================
# type()
# ==========================================================

age = 18

print(type(age))

# Output

# <class 'int'>

# type() returns the data type of the variable.


# ==========================================================
# id()
# ==========================================================

x = 10

print(id(x))

# Output

# Different number every execution

# id() returns the memory identity of the object.


# ==========================================================
# MULTIPLE ASSIGNMENT
# ==========================================================

a, b, c = 10, 20, 30

print(a)
print(b)
print(c)

# Output

# 10
# 20
# 30


# ==========================================================
# SWAPPING VARIABLES
# ==========================================================

a = 10
b = 20

a, b = b, a

print(a)
print(b)

# Output

# 20
# 10

# Python swaps variables without using a temporary variable.


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# Variable stores data.

# Python is Dynamically Typed.

# type() returns the data type.

# id() returns the memory identity.

# int()
# float()
# str()
# bool()

# are used for Type Casting.

# ==========================================================
# INTERVIEW QUESTIONS
# ==========================================================
# Q1. What is a Variable?
# Q2. What is Dynamic Typing?
# Q3. Difference between int and float?
# Q4. Difference between None and 0?
# Q5. What does type() return?
# Q6. What does id() return?
# Q7. How do you swap two variables?
# Q8. What is Multiple Assignment?
# 09. Can one variable store different data types?
# Q10. What is None?


