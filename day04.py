# Type casting in python
# Type casting is the process of converting one data type to another data type. In python, we can use the built-in functions to perform type casting.

a = "1"
b = "2"
print(a + b)
 # output: 12
# integer cannot be added to string, so we need to convert the string to integer using int() function

print(int(a) + int(b)) 
 # exlpicit type casting, output: 3

c = 1.09
d = 8
print(c + d) 
# output: 9.09 , implicit type casting, python automatically converts the integer to float and then adds them

