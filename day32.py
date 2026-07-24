# Enumerate Functions in python

marks = [34, 38, 90, 98, 12, 45, 18, 77, 1]

index = 0
for mark in marks:
    print(mark)
    if(index == 3):
        print("awesome , Bhalbheem")
    index += 1



for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
         print("awesome , Bhalbheem")
    index += 1
        


for index, mark in enumerate(marks, start = 1):
    print(index, mark)