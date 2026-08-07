# ==========================================================
# PYTHON DAY 4
# TYPE CASTING
# ==========================================================

# ==========================================================
# TYPE CASTING
# ==========================================================

# Type Casting:
# Type Casting is the process of converting one data type into another.

# Examples

age = "18"

print(type(age))

# Output

# <class 'str'>


# ==========================================================
# STRING -> INTEGER
# ==========================================================

age = "18"

new_age = int(age)

print(new_age)
print(type(new_age))

# Output

# 18
# <class 'int'>


# ==========================================================
# INTEGER -> STRING
# ==========================================================

age = 18

new_age = str(age)

print(new_age)
print(type(new_age))

# Output

# 18
# <class 'str'>


# ==========================================================
# INTEGER -> FLOAT
# ==========================================================

number = 10

new_number = float(number)

print(new_number)
print(type(new_number))

# Output

# 10.0
# <class 'float'>


# ==========================================================
# FLOAT -> INTEGER
# ==========================================================

number = 99.99

new_number = int(number)

print(new_number)
print(type(new_number))

# Output

# 99
# <class 'int'>

# int() removes the decimal part.
# It DOES NOT round the number.


# ==========================================================
# FLOAT -> STRING
# ==========================================================

price = 99.99

new_price = str(price)

print(new_price)
print(type(new_price))

# Output

# 99.99
# <class 'str'>


# ==========================================================
# STRING -> FLOAT
# ==========================================================

price = "99.99"

new_price = float(price)

print(new_price)
print(type(new_price))

# Output

# 99.99
# <class 'float'>


# ==========================================================
# BOOLEAN TYPE CASTING
# ==========================================================

print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Python"))

# Output

# True
# False
# False
# True


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# int()     -> Converts into Integer

# float()   -> Converts into Float

# str()     -> Converts into String

# bool()    -> Converts into Boolean

# int() removes decimal values.

# Invalid conversion raises ValueError.


# ==========================================================
# INVALID TYPE CASTING
# ==========================================================

# Example

number = "Python"

# print(int(number))

# Output

# ValueError

# Because "Python" cannot be converted into Integer.
