# Lists in python

l = [3,4,5,"bhalbheem",True]
print(type(l))
print(l)

print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])

print(l[-3])# Negative index
print(l[len(l)-3])# same output but positive index

if 3 in l:
    print("yes")
else:
    print("No")

if "bhal" in "bhalbheem":
    print("yes")

# jump index
print(l[1:5:2])


# list comprehension
lst = [i*i for i in range(8)]
print(lst)
lst = [i*i for i in range(8) if i%2 == 0]
print(lst)