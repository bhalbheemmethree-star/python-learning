# Functions in python

a = 5
b = 8
gmean = (a*b)/(a+b)
print(gmean)


a = 5
b = 8
if(a>b):
    print("first number is greater")
else:
    print("second number is greater or equal")


# to avoid writing the same code again and again we use functions in python

def calculategmean(a,b):
    gmean = (a*b)/(a+b)
    print(gmean)


def isgreater(a,b):
    if(a>b):
        print("first number is greater")
    else:
        print("second number is greater or equal")


def islesser(a,b):
    pass
# by writing pass it doesnt give error and we can write the code later on


a = 5
b = 8
calculategmean(a,b)
isgreater(a,b)

c = 8 
d = 7
calculategmean(c,d)
isgreater(c,d)

