# ==========================================================
# PYTHON DAY 12
# WHILE LOOP
# ==========================================================


# ==========================================================
# WHILE LOOP
# ==========================================================

# A while loop repeatedly executes a block of code
# as long as the given condition is True.

# Syntax:

# while condition:
#     code


# ==========================================================
# BASIC WHILE LOOP
# ==========================================================

i = 1

while i <= 5:
    print(i)
    i += 1

# Output

# 1
# 2
# 3
# 4
# 5

# The loop continues while the condition is True.
# i += 1 updates the value so the loop can eventually stop.


# ==========================================================
# COUNTER WITH WHILE LOOP
# ==========================================================

count = 1

while count <= 3:
    print("Hello")
    count += 1

# Output

# Hello
# Hello
# Hello

# A counter is commonly used to control a while loop.


# ==========================================================
# UPDATING THE COUNTER
# ==========================================================

number = 1

while number <= 5:
    print(number)
    number += 1

# number += 1 increases number by 1
# after every iteration.


# ==========================================================
# COUNTING BACKWARDS
# ==========================================================

number = 5

while number >= 1:
    print(number)
    number -= 1

# Output

# 5
# 4
# 3
# 2
# 1

# The counter can also be decreased.


# ==========================================================
# WHILE WITH A CONDITION
# ==========================================================

age = 15

while age < 18:
    print("Age:", age)
    age += 1

# Output

# Age: 15
# Age: 16
# Age: 17


# ==========================================================
# WHILE WITH USER INPUT
# ==========================================================

number = int(input("Enter a number: "))

while number != 0:
    print("You entered:", number)
    number = int(input("Enter another number: "))

# The loop continues until the user enters 0.


# ==========================================================
# INFINITE LOOP
# ==========================================================

# If the condition never becomes False,
# the while loop runs forever.

# Example:

# i = 1
#
# while i <= 5:
#     print(i)

# This becomes an infinite loop because
# i is never changed.


# ==========================================================
# STOPPING AN INFINITE LOOP
# ==========================================================

i = 1

while i <= 5:
    print(i)
    i += 1

# Updating the variable makes the condition
# eventually become False.


# ==========================================================
# break
# ==========================================================

# break immediately stops the while loop.

i = 1

while i <= 10:
    if i == 5:
        break

    print(i)
    i += 1

# Output

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

i = 0

while i < 5:
    i += 1

    if i == 3:
        continue

    print(i)

# Output

# 1
# 2
# 4
# 5

# 3 is skipped.


# ==========================================================
# pass
# ==========================================================

# pass does nothing.
# It is used as a placeholder.

i = 1

while i <= 3:
    pass

# WARNING:
# This is an infinite loop because i is never updated.

# A safe example:

i = 1

while i <= 3:
    if i == 2:
        pass

    print(i)
    i += 1

# Output

# 1
# 2
# 3


# ==========================================================
# break vs continue vs pass
# ==========================================================

# break    -> Stops the entire loop.

# continue -> Skips the current iteration.

# pass     -> Does nothing.


# ==========================================================
# NESTED WHILE LOOP
# ==========================================================

# A while loop inside another while loop
# is called a nested while loop.

i = 1

while i <= 2:
    j = 1

    while j <= 3:
        print(i, j)
        j += 1

    i += 1

# Output

# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3

# The inner loop completes its iterations
# for every iteration of the outer loop.


# ==========================================================
# WHILE WITH if
# ==========================================================

number = 1

while number <= 10:

    if number % 2 == 0:
        print(number)

    number += 1

# Output

# 2
# 4
# 6
# 8
# 10


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# while loop -> Repeats code while a condition is True.

# The condition is checked before every iteration.

# The loop should usually update the variable
# used in its condition.

# If the condition never becomes False,
# the loop can become infinite.

# break -> Stops the loop.

# continue -> Skips the current iteration.

# pass -> Does nothing.

# Nested while -> while loop inside another while loop.


# ==========================================================
# COMMON MISTAKES
# ==========================================================

# Mistake 1:
# Forgetting to update the counter.

# Wrong:

# i = 1
#
# while i <= 5:
#     print(i)

# This creates an infinite loop.


# Correct:

i = 1

while i <= 5:
    print(i)
    i += 1


# Mistake 2:
# Incorrect indentation.

# Correct:

i = 1

while i <= 3:
    print(i)
    i += 1


# Mistake 3:
# Using continue before updating the counter.

# This can create an infinite loop.

# Correct:

i = 0

while i < 5:
    i += 1

    if i == 3:
        continue

    print(i)

