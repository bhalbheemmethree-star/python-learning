with open('myfile.txt', 'r') as f:
    text = f.readline()
    print(text) # prints the content of the file after writing and appending only the first line of the file


with open("myfile.txt", "r") as f:
    for line in f:
        print(line)
# This will print all the lines in the file one by one. The 'with' statement ensures that the file is properly closed after its suite finishes, even if an exception is raised at some point.