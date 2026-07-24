# Raising costum errors in python

a = int(input("Enter any value between 5 and 9: "))

if (a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")


print("Hey i am bhalbheem methree")

# this error we raise wantedly because the code should stop running if any input wont work 