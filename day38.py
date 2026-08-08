# FILE I/O in python

f = open('myfile.txt', 'r')
text = f.read()
print(text) # prints the content of the file

a = open('myfile2.txt', 'x')
b = open('myfile3.txt', 'w') 
# this both will create a new file if it does not exist, but 'x' will raise an error if the file already exists, while 'w' will overwrite the existing file.

with open('myfile.txt', 'w') as f:
    f.write('Hello, World!') # completely replace with new code 


with open('myfile.txt', 'a') as f:
    f.write('\nThis is an appended line.') # appends to the file and automatically closes it after the block