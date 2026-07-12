# Tuples in python
# tuple should contain , or it will be integer
#  tuples are unchangble

tup = (1,6,"green",True) # tuple should contain , or it will be integer
# tup[0] = 12 # this shows an error it cannot change or add element in tuple
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])

if "green" in tup: 
    print("yes its present in the tuple")
else:
    print("its not present in the tuple")

tup2 = tup[0:3]
print(tup2)