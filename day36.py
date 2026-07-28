# os module in python
 
import os

if not os.path.exists("data"):
    os.mkdir("data") # create folder

if not os.path.exists("delete_demo"):
    os.mkdir("delete_demo") # create folder
 

for i in range (0, 100):
    os.mkdir(f"data/day{i+1}") #creates file
    os.rename(f"data/day{i+1}", f"data/tutorial{i+1}") # rename files 


folders = os.listdir("data") #prints all files created in data
print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))


print(os.getcwd()) # prints  the Current Working Directory (CWD).
os.chdir("data") # used to change directory
print(os.getcwd()) # directory after changing

os.rmdir("delete_demo") # deletes folder
