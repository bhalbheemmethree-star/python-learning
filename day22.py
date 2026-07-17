# Recursion in Python
'''Recursion is a programming technique where a function calls
 itself to solve a larger problem by breaking it down into smaller,
  more manageable subproblems'''


def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else :
        return (n * factorial(n- 1))

print(factorial(5))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1 * factorial(0)


# fibonacci sequence 
# f(0) = 0
# f(1) = 1
# f(2) = f(0) + f(1)
# f(n) = f(n-1) + f(n-2)

# program for fibonacci sequence
def fibonacci(n):
    if (n == 0 ):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print (fibonacci(10))