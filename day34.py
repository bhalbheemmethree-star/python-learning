# # how import works in python

# import math
# result = math.factorial(10)
# print(result)

# x = math.sqrt(9)
# print(x)


# # the as keyword we can use module name in shortcut
# import math as a 
# result = a.factorial(10)
# print(result)

# # we can print all functions in a module
# print(dir(math))


from main import welcome, harry

welcome()
print(harry)

# prints
# hey welcome my friend
# a good boy

# because the main.py file has 
def welcome():
    print("hey welcome my friend")

harry = "a good boy"