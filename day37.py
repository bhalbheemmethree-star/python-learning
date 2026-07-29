# Local vs global variables in python

'''the variable outside the function can used in function unless the same variable
in that function is called global variable and the variable exist in function
we cannot use it outside of function'''

# x = 4 # global variable
# print(x)

# def hello():
#     x = 1 # local variable
#     print(f"the local x is {x}")
#     print("hello bro")

# hello()
# print(f"the global x is {x}")

# global keyword
''' this keyword is used inside of function if we use this keyword and variable
it ignores the actual global variable and prints which is in this keyword'''


x = 10 # actual global variable

def my_function():
    global x
    x = 20
    y = 15
    print(y)

my_function()
print(x)