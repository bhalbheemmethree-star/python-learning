# For loops in python 

name = "bhalbheem"
for i in name:
    print(i)

for i in name:
    print(i, end=",")


colours = ["red", "green", "blue", "yellow"]
for color in colours:
    print(color)
    for i in color:
        print(i)


for x in range(5):    # this prints 1 to 4 
    print(x)

for x in range(5):
    print(x + 1)     # this prints 1 to 5