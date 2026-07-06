#day 09: If else conditional statements in python
# conditional operators
# > , < , >= , <= , == , !=  

a = int(input("Enter your age :"))
print("your age is ", a)

print(a>18)
print(a<18)
print(a>=18)
print(a<=18)
print(a==18)
print(a!=18)

if(a>18):
    print("you can drive")
else:
    print("you cannot drive")


appleprice = 210
budget = 200
if (appleprice <= budget):
    print("you can buy apple")
else:
    print("you cannot buy apple")


num = int(input("Enter the value of num :"))

if (num < 0):
    print("number is negative")
elif(num == 0):
    print("number is zero")
elif(num == 999):
    print("number is special")
else:
    print("number is positive")

print("i am happy now")



num = 18
if (num < 0):
    print("number is negative")
elif(num > 0):
    if(num <= 10):
        print("number is between 1 - 10")
    elif(num >= 10 and num <= 20):
        print("number is between 11 - 20")
    else:
        print("number is greater than 20")
else:
    print("number is zero")