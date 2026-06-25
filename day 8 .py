# string methods in Python
# Strings are immutable 

a = "Bhal bheem"
b = "!!!rohit!!!!!!"
c = "machine"
print(len(a))
# it prints the number of characters  in string
print(a.upper())
# prints all the letters in upper case in a string
print(a.lower())
# prints all the letters in lower case in a string
print(b.rstrip("!"))
# removes the specific character from a string
print(a.replace("Bhalbheem","developer"))
# replace all occurance of string with another string
print(a.split(" "))
# splits the specified instance and returns the seperated strings as a list items
print(c.capitalize())
# this converts only first letter of string into upper case
print(c.center(10))
# this can change the length of a string as we entered 10 now length of string "c" is 10
print(a.count("h"))
# this counts the specified character used in the string
print(b.endswith("!!!!!!"))
#  if string ends with given specified value it prints true or prints false
print(a.find("e")) # prints -1 if character not found in a string
# it finds the specific character in a string and prints the number
print(a.index(z))
# this prints value error 
print(a.isalnum()) # even space in string also a false
# if the strings contains A-Z,a-z,0-9 it prints true if any other character it prints false
print(c.isalpha())
# if the string contains A-Z,a-z it prints true if any number or other character it prints false
print(c.islower())
# if all the characters in string are in lower case it prints true or it prints false
print(b.isprintable())
# if string is printable it prints true or false
print(a.isspace())
# if string contains only empty space prints true or if any other character prints false
print(a.istitle())
# prints true if first letter of all words in a string is capitalized or prints false
print(a.isupper())
# prints true if all characters in a string are in uppercase or prints false
print(a.startswith("B"))
# id string starts with soecified character prints true or prints 
print(a.swapcase())
# this changes the character casing upper to lower and vice versa
print(a.title())
# this captalize the first letter of every word in a string