# ==========================================================
# PYTHON DAY 13
# LOOP CONTROL STATEMENTS
# ==========================================================


# ==========================================================
# LOOP CONTROL STATEMENTS
# ==========================================================

# Loop control statements change the normal execution
# of a loop.

# Python has three important loop control statements:

# break
# continue
# pass


# ==========================================================
# break
# ==========================================================

# break immediately stops the entire loop.

for i in range(1, 10):
    if i == 5:
        break

    print(i)

# Output

# 1
# 2
# 3
# 4

# When i becomes 5, break stops the loop completely.


# ==========================================================
# break WITH while
# ==========================================================

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


# ==========================================================
# continue
# ==========================================================

# continue skips the current iteration
# and moves to the next iteration.

for i in range(1, 6):
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
# continue WITH while
# ==========================================================

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
# It is used as a placeholder when Python
# requires a statement but you don't want
# to execute anything yet.

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
# pass WITH while
# ==========================================================

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
# DIFFERENCE BETWEEN break, continue AND pass
# ==========================================================

# break
# -> Stops the entire loop.

for i in range(5):
    if i == 2:
        break

    print(i)

# Output:
# 0
# 1


# continue
# -> Skips only the current iteration.

for i in range(5):
    if i == 2:
        continue

    print(i)

# Output:
# 0
# 1
# 3
# 4


# pass
# -> Does nothing.

for i in range(5):
    if i == 2:
        pass

    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4


# ==========================================================
# break IN A NESTED LOOP
# ==========================================================

for i in range(3):

    for j in range(3):

        if j == 1:
            break

        print(i, j)

# Output

# 0 0
# 1 0
# 2 0

# break stops only the loop in which it is written.
# It does not automatically stop all outer loops.


# ==========================================================
# continue IN A NESTED LOOP
# ==========================================================

for i in range(2):

    for j in range(3):

        if j == 1:
            continue

        print(i, j)

# Output

# 0 0
# 0 2
# 1 0
# 1 2

# continue skips the current iteration
# of the loop in which it appears.


# ==========================================================
# IMPORTANT WARNING WITH continue
# ==========================================================

# Be careful when using continue in a while loop.

# Wrong:

# i = 0
#
# while i < 5:
#     if i == 3:
#         continue
#
#     i += 1

# When i becomes 3, continue runs before i is updated.
# This creates an infinite loop.


# Correct:

i = 0

while i < 5:
    i += 1

    if i == 3:
        continue

    print(i)


# ==========================================================
# QUICK REVISION
# ==========================================================

# break    -> STOP the entire loop

# continue -> SKIP the current iteration

# pass     -> DO NOTHING
