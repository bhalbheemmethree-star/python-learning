# dictionaries in python
# dictionary is ordered collection set of key value pairs

dic = {
    "Rohit": "Human being",
    "spoon":"Object"

}
print(dic)
print(dic["Rohit"])

dict = {
    310: "bhalbheem",
    285: "rohit",
    432: "king"

}
print(dict)
print(dict[432])


info = {'name': 'karan', 'age': 19 , 'eligible': True}
print(info['name']) # prints value but shows error if wrong key given
print(info.get('boy')) # prints value but doesnt show error if wrong key given and shows none
print(info.keys()) # prints all the keys 
print(info.values()) # prints all the values
print(info.items()) # prints each key value pair seperately


for value in info.values():
    print([value])
# this print the value of keys

for key in info.keys():
    print([key])
# this prints keys 


for key in info.keys():
    print(f"The value corresponding to the {key} is {info[key]}")


for key , value in info.items():
    print(f"The value corresponding to the {key} is {value}")