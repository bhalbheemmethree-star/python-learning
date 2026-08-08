# readline()

with open('myfile.txt', 'r') as f:
    text = f.readline()
    print(text)  # reads only the first line

# Example

# myfile.txt

# Python
# SQL
# PostgreSQL
# Django

# Output

# Python

# every call reads the next line

with open('myfile.txt', 'r') as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())

# Output

# Python
# SQL
# PostgreSQL

# readline() returns a STRING

# when end of file is reached,
# readline() returns ""

# readlines()

with open('myfile.txt', 'r') as f:
    text = f.readlines()
    print(text)

# Example

# myfile.txt

# Python
# SQL
# PostgreSQL
# Django

# Output

# ['Python\n', 'SQL\n', 'PostgreSQL\n', 'Django']

# readlines() returns a LIST

with open('myfile.txt', 'r') as f:
    data = f.readlines()

print(data[0])
print(data[1])

# Output

# Python
# SQL

# write()

with open('myfile.txt', 'w') as f:
    f.write("Python")

# Output File

# Python

# write() writes ONE string

# writing multiple strings

with open('myfile.txt', 'w') as f:
    f.write("Python\n")
    f.write("SQL\n")
    f.write("PostgreSQL")

# Output File

# Python
# SQL
# PostgreSQL

# write() returns the number of characters written

# writelines()

languages = [
    "Python\n",
    "SQL\n",
    "PostgreSQL\n",
    "Django\n"
]

with open('myfile.txt', 'w') as f:
    f.writelines(languages)

# Output File

# Python
# SQL
# PostgreSQL
# Django

# writelines() writes multiple strings from a LIST

# writelines() DOES NOT automatically add '\n'

languages = [
    "Python",
    "SQL",
    "PostgreSQL"
]

with open('myfile.txt', 'w') as f:
    f.writelines(languages)

# Output File

# PythonSQLPostgreSQL

# therefore add '\n' manually
