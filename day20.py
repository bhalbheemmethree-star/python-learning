# f strings in python
 
# string formatting
letter = "Hey my name is {} and i live in {}"
name = "bhal bheem"
country = "india"
print(letter.format(name , country))

letter = "Hey my name is {1} and i live in {0}"
name = "bhal bheem"
country = "india"
print(letter.format(country , name ))

txt = "for only {price:.2f} dollars!" # 2f indicates that only 2 decimal points
print(txt.format(price = 19.09999999))

# now f string
print(f"Hey my name is {name} and i live in {country}")
print(f"Hey my name is {{name}} and i live in {{country}}")


