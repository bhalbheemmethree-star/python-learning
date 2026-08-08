# ==========================================================
# PYTHON DAY 11
# FOR LOOP
# ==========================================================


# ==========================================================
# FOR LOOP
# ==========================================================

# A for loop is used to repeat a block of code
# for every item in a sequence or iterable.

# Syntax:

# for variable in sequence:
#     code


# ==========================================================
# BASIC FOR LOOP
# ==========================================================

for i in range(5):
    print(i)

# Output

# 0
# 1
# 2
# 3
# 4

# range(5) generates numbers from 0 to 4.
# The stop value is not included.


# ==========================================================
# FOR LOOP WITH A STRING
# ==========================================================

name = "Python"

for char in name:
    print(char)

# Output

# P
# y
# t
# h
# o
# n

# The loop processes each character one by one.


# ==========================================================
# range()
# ==========================================================

# range() generates a sequence of numbers.

for i in range(5):
    print(i)

# Output

# 0
# 1
# 2
# 3
# 4


# ==========================================================
# range(start, stop)
# ==========================================================

for i in range(2, 6):
    print(i)

# Output

# 2
# 3
# 4
# 5

# start is included.
# stop is not included.


# ==========================================================
# range(start, stop, step)
# ==========================================================

for i in range(1, 10, 2):
    print(i)

# Output

# 1
# 3
# 5
# 7
# 9

# step determines how much the value changes each time.


# ==========================================================
# REVERSE FOR LOOP
# ==========================================================

for i in range(5, 0, -1):
    print(i)

# Output

# 5
# 4
# 3
# 2
# 1

# A negative step moves backwards.


# ==========================================================
# PRINT EVEN NUMBERS
# ==========================================================

for i in range(2, 11, 2):
    print(i)

# Output

# 2
# 4
# 6
# 8
# 10


# ==========================================================
# PRINT ODD NUMBERS
# ==========================================================

for i in range(1, 10, 2):
    print(i)

# Output

# 1
# 3
# 5
# 7
# 9


# ==========================================================
# FOR LOOP WITH if
# ==========================================================

for i in range(1, 6):
    if i % 2 == 0:
        print(i)

# Output

# 2
# 4

# A condition can be used inside a for loop.


# ==========================================================
# NESTED FOR LOOP
# ==========================================================

# A for loop inside another for loop
# is called a nested loop.

for i in range(3):
    for j in range(2):
        print(i, j)

# Output

# 0 0
# 0 1
# 1 0
# 1 1
# 2 0
# 2 1

# The inner loop runs completely
# for every iteration of the outer loop.


# ==========================================================
# break
# ==========================================================

# break immediately stops the loop.

for i in range(10):
    if i == 5:
        break
    print(i)

# Output

# 0
# 1
# 2
# 3
# 4

# The loop stops when i becomes 5.


# ==========================================================
# continue
# ==========================================================

# continue skips the current iteration
# and moves to the next iteration.

for i in range(5):
    if i == 2:
        continue
    print(i)

# Output

# 0
# 1
# 3
# 4

# 2 is skipped.


# ==========================================================
# pass
# ==========================================================

# pass does nothing.
# It is used as a placeholder.

for i in range(5):
    if i == 2:
        pass
    print(i)

# Output

# 0
# 1
# 2
# 3
# 4

# pass does not stop or skip the loop.


# ==========================================================
# break vs continue vs pass
# ==========================================================

# break    -> Stops the entire loop.

# continue -> Skips the current iteration.

# pass     -> Does nothing.

# ==========================================================
# else WITH break
# ==========================================================

for i in range(5):
    if i == 2:
        break
    print(i)
else:
    print("Loop completed")

# Output

# 0
# 1

# The else block does NOT execute
# because the loop was stopped by break.


# ==========================================================
# ITERATING THROUGH A LIST
# ==========================================================

numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)

# Output

# 10
# 20
# 30
# 40

# A for loop can process each item
# in a sequence one by one.


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# for loop -> Repeats code for each item.

# range(n) -> 0 to n-1

# range(start, stop) -> start to stop-1

# range(start, stop, step) -> Uses a custom step.

# Negative step -> Moves backwards.

# break -> Stops the loop.

# continue -> Skips the current iteration.

# pass -> Does nothing.

# Nested loop -> Loop inside another loop.

# for-else -> else runs when the loop
#             completes normally.


# ==========================================================
# COMMON MISTAKES
# ==========================================================

# Wrong:

# for i in range(5)
#     print(i)

# Missing colon (:)


# Correct:

for i in range(5):
    print(i)


# Wrong:

# for i in range(5):
# print(i)

# Incorrect indentation.


# Correct:

for i in range(5):
    print(i)

