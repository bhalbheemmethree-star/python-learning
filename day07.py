# ==========================================================
# PYTHON DAY 7
# STRING INDEXING, SLICING & OPERATIONS
# ==========================================================


# ==========================================================
# STRING INDEXING
# ==========================================================

# Indexing:
# Each character in a string has a position called an index.

name = "Python"

# P  y  t  h  o  n
# 0  1  2  3  4  5

print(name[0])
print(name[2])
print(name[5])

# Output

# P
# t
# n


# ==========================================================
# NEGATIVE INDEXING
# ==========================================================

# Negative indexing starts from the end of the string.

name = "Python"

# P   y   t   h   o   n
# -6 -5  -4  -3  -2  -1

print(name[-1])
print(name[-2])

# Output

# n
# o


# ==========================================================
# STRING SLICING
# ==========================================================

# Slicing is used to extract a part of a string.

# Syntax

# string[start:stop]

# start is included
# stop is NOT included

name = "Python"

print(name[0:3])

# Output

# Pyt


# ==========================================================
# OMITTING START
# ==========================================================

name = "Python"

print(name[:3])

# Output

# Pyt

# If start is omitted,
# slicing starts from the beginning.


# ==========================================================
# OMITTING STOP
# ==========================================================

name = "Python"

print(name[2:])

# Output

# thon

# If stop is omitted,
# slicing continues until the end.


# ==========================================================
# STRING SLICING WITH STEP
# ==========================================================

# Syntax

# string[start:stop:step]

name = "Python"

print(name[0:6:2])

# Output

# Pto

# Step decides how many positions to move each time.


# ==========================================================
# REVERSE A STRING
# ==========================================================

name = "Python"

print(name[::-1])

# Output

# nohtyP

# -1 moves through the string backwards.


# ==========================================================
# STRING CONCATENATION
# ==========================================================

# Concatenation means joining strings together.

first_name = "Bhalbheem"
last_name = "Methree"

full_name = first_name + " " + last_name

print(full_name)

# Output

# Bhalbheem Methree


# ==========================================================
# STRING REPETITION
# ==========================================================

# * can be used to repeat a string.

word = "Hi "

print(word * 3)

# Output

# Hi Hi Hi


# ==========================================================
# in OPERATOR
# ==========================================================

# Used to check whether a character or substring
# exists inside a string.

name = "Python"

print("P" in name)
print("z" in name)

# Output

# True
# False


# ==========================================================
# not in OPERATOR
# ==========================================================

name = "Python"

print("z" not in name)

# Output

# True

# not in checks whether something does NOT exist
# inside the string.


# ==========================================================
# STRING COMPARISON
# ==========================================================

a = "apple"
b = "banana"

print(a == b)
print(a != b)

# Output

# False
# True

# Strings can be compared using comparison operators.


# ==========================================================
# INDEXING VS SLICING
# ==========================================================

name = "Python"

print(name[0])

# Output

# P

print(name[0:1])

# Output

# P

# Indexing returns a character.
# Slicing returns a part of the string.


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# Indexing → Access a character using its position.

# Positive indexing → Starts from 0.

# Negative indexing → Starts from -1.

# Slicing → Extracts a part of a string.

# string[start:stop]
# start is included.
# stop is excluded.

# string[start:stop:step]
# step controls the movement between characters.

# [::-1] → Reverses a string.

# + → Concatenates strings.

# * → Repeats strings.

# in → Checks whether something exists.

# not in → Checks whether something does not exist.
