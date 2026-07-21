# For loop with else in python

for i in ():
    print(i)
else:
    print("sorry no i")


for i in range(4):
    print(i)
    if i == 2:
        break
else:
    print("sorry no i ")


i = 0
while i<4:
    print(i)
    i = i + 1 
    if i == 2:
        break
else:
    print("sorry no i")



for x in range(5):
    print("itration no {} in for loop".format(x + 1))
else:
    print("else block in loop")

print("out of the loop")