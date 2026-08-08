# ==========================================================
# PYTHON DAY 9
# IF, ELIF & ELSE STATEMENTS
# ==========================================================


# ==========================================================
# CONDITIONAL STATEMENTS
# ==========================================================

# Conditional statements are used to make decisions
# in a program based on a condition.

# Python checks the condition.
# If the condition is True, the corresponding block runs.


# ==========================================================
# if STATEMENT
# ==========================================================

# Syntax

# if condition:
#     statement

age = 18

if age >= 18:
    print("You are eligible")

# Output

# You are eligible

# The code inside the if block runs only when
# the condition is True.


# ==========================================================
# INDENTATION
# ==========================================================

age = 20

if age >= 18:
    print("Adult")

# Indentation tells Python which statements
# belong to the if block.

# Python normally uses 4 spaces for indentation.


# ==========================================================
# if WITH FALSE CONDITION
# ==========================================================

age = 15

if age >= 18:
    print("Adult")

# Nothing is printed because the condition is False.


# ==========================================================
# else STATEMENT
# ==========================================================

# else runs when the if condition is False.

age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")

# Output

# Minor


# ==========================================================
# if-else
# ==========================================================

number = 10

if number > 0:
    print("Positive")
else:
    print("Not Positive")

# Output

# Positive


# ==========================================================
# elif STATEMENT
# ==========================================================

# elif means "else if".

# It is used when we want to check multiple conditions.

marks = 75

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")

# Output

# B

# Python checks conditions from top to bottom.
# The first True condition is executed.


# ==========================================================
# MULTIPLE elif
# ==========================================================

age = 25

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")

# Output

# Adult


# ==========================================================
# COMPARISON OPERATORS IN CONDITIONS
# ==========================================================

age = 20

if age == 20:
    print("Age is 20")

# Common comparison operators:

# >   Greater than
# <   Less than
# >=  Greater than or equal to
# <=  Less than or equal to
# ==  Equal to
# !=  Not equal to


# ==========================================================
# CONDITIONS WITH STRINGS
# ==========================================================

name = "Bhalbheem"

if name == "Bhalbheem":
    print("Correct name")
else:
    print("Different name")

# Output

# Correct name


# ==========================================================
# NESTED if
# ==========================================================

# An if statement inside another if statement
# is called a nested if.

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Underage")

# Output

# Entry allowed


# ==========================================================
# if WITH USER INPUT
# ==========================================================

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible")
else:
    print("Not eligible")


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# if      -> Checks a condition

# elif    -> Checks another condition
#            when previous conditions are False

# else    -> Runs when all previous conditions are False

# Indentation is required in Python.

# Only the first True condition in an if/elif chain runs.

# else does not have a condition.


# ==========================================================
# COMMON MISTAKES
# ==========================================================

# Wrong:

# if age >= 18
#     print("Adult")

# Missing colon (:)


# Correct:

age = 18

if age >= 18:
    print("Adult")


# Wrong indentation:

# if age >= 18:
# print("Adult")

# Correct:

if age >= 18:
    print("Adult")

