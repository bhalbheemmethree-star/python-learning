# ==========================================================
# PYTHON DAY 5
# TAKING USER INPUT
# ==========================================================

# ==========================================================
# input()
# ==========================================================

# input():
# Used to take input from the user.

name = input("Enter your name: ")

print(name)

# Example

# Input

# Bhalbheem

# Output

# Bhalbheem


# ==========================================================
# input() ALWAYS RETURNS STRING
# ==========================================================

age = input("Enter your age: ")

print(type(age))

# Input

# 18

# Output

# <class 'str'>

# Even if the user enters a number,
# input() always returns a STRING.


# ==========================================================
# INTEGER INPUT
# ==========================================================

age = int(input("Enter your age: "))

print(age)
print(type(age))

# Input

# 18

# Output

# 18
# <class 'int'>


# ==========================================================
# FLOAT INPUT
# ==========================================================

height = float(input("Enter your height: "))

print(height)

# Input

# 180.5

# Output

# 180.5


# ==========================================================
# MULTIPLE INPUTS
# ==========================================================

name = input("Enter Name: ")
age = int(input("Enter Age: "))
height = float(input("Enter Height: "))

print(name)
print(age)
print(height)


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# input() takes input from the user.

# input() always returns String.

# Use int() for Integer input.

# Use float() for Decimal input.

# Use str() only if needed because
# input() already returns String.


# ==========================================================
# COMMON MISTAKES
# ==========================================================

age = input("Enter age: ")

# Wrong

print(age + 10)

# Error

# Correct

age = int(input("Enter age: "))

print(age + 10)
