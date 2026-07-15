# Recursion in python

def numbers(n):
    if n == 0:
        return

    print(n)
    numbers(n - 1)