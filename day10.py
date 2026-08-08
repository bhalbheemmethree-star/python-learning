# ==========================================================
# PYTHON DAY 10
# MATCH-CASE STATEMENT
# ==========================================================


# ==========================================================
# WHAT IS match-case?
# ==========================================================

# match-case is used to compare a value with
# different possible patterns.

# It is similar to switch statements in other languages.


# ==========================================================
# BASIC SYNTAX
# ==========================================================

# match value:
#     case pattern:
#         statement
#     case pattern:
#         statement
#     case _:
#         statement


# ==========================================================
# BASIC EXAMPLE
# ==========================================================

day = 1

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")

# Output

# Monday


# ==========================================================
# case _
# ==========================================================

# _ works as the default case.
# It runs when none of the previous cases match.

day = 7

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Other day")

# Output

# Other day


# ==========================================================
# MATCH-CASE WITH STRINGS
# ==========================================================

command = "start"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "pause":
        print("Paused")
    case _:
        print("Unknown command")

# Output

# Starting...


# ==========================================================
# MATCH-CASE WITH USER INPUT
# ==========================================================

choice = input("Enter your choice: ")

match choice:
    case "1":
        print("Add")
    case "2":
        print("View")
    case "3":
        print("Delete")
    case _:
        print("Invalid choice")


# ==========================================================
# MULTIPLE VALUES IN ONE CASE
# ==========================================================

day = 6

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid day")

# Output

# Weekend

# | means OR inside a match pattern.


# ==========================================================
# MATCH-CASE WITH CONDITIONS
# ==========================================================

age = 20

match age:
    case age if age >= 18:
        print("Adult")
    case _:
        print("Minor")

# Output

# Adult

# A guard (if condition) can be used with a case.


# ==========================================================
# MATCH-CASE VS if-elif-else
# ==========================================================

# if-elif-else

choice = 2

if choice == 1:
    print("Add")
elif choice == 2:
    print("View")
else:
    print("Invalid")


# match-case

match choice:
    case 1:
        print("Add")
    case 2:
        print("View")
    case _:
        print("Invalid")

# Both can make decisions.
# match-case is especially useful when
# comparing one value against multiple patterns.


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# match -> value that we want to compare

# case  -> pattern that we want to match

# _     -> default case

# |     -> matches multiple patterns

# A case can also have an if condition (guard).

# match-case was introduced in Python 3.10.

# match-case is not exactly the same as
# switch statements in every other language.
# Python's match-case supports pattern matching.


# ==========================================================
# COMMON MISTAKES
# ==========================================================

# Wrong:

# match day
#     case 1:
#         print("Monday")

# Missing colon after match expression.

# Correct:

day = 1

match day:
    case 1:
        print("Monday")

