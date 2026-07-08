# Function Arguments and return statements in python

def average(a,b):
    print("The average is, ", (a+b)/2)

average(5,6)

# Default arguments in python
def average(a=2,b=4):
    print("The average is ", (a+b)/2)

average() # here a will take default value 2 and b will take value 8

# keyword arguments in python
def average(a=8,b=2):
    print("The average is ", (a+b)/2)

average(b=4,a=12)# here a will take value 12 and b will take value 4 

# Required arguments in python
def average(a,b=8):
    print("The average is ", (a+b)/2)

average(a=2) # here a will take value 2 and b will take default value 8

# Positional arguments in python
def average(a,b,c=1):
    print("The average is ", (a+b+c)/3)

average(2,8) # here a will take value 2 and b will take value 8 and c will take default value 1

#  Variable length arguments in python
def Average(*numbers):  #for tuple type of arguments we use * before the variable name
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("The average is ", sum / len(numbers))

Average(2,8,4,6,10) 



def name(**name):  # for dictionary type of arguments we use ** before the variable name
    print(type(name))
    print("The name is ", name['first'], name['last'])

name(first="Bhalbheem", last="Methree")


# Return statement
def Average(*numbers): 
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)

c = Average(2,8,4,6,10) 
print(c)