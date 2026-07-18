# Sets in python
# doesnt print repeated values
# sets are unchangeble
''' a set is a built-in data type that represents an unordered 
collection of unique elements'''

s = {1,5,3,2,5,5}
print(s)

info = {"bhalbheem",57,19.9,False,57}
print(info)

a = {}
print(type(a))
# this prints dict

a = set()
print(type(a))
# this prints set


for value in info:
    print(value)