# Lists methods in python
l = [1,5,9,2,6,1]
l.append(7) # it adds the specific element at the end of the list 
l.sort(reverse=True) # it sorts acending or decending order based on false or true statement
l.reverse() # it reverses the list
print(l.index(9)) # it print the index of specific element from a list
print(l.count(1)) # it prints the count of specific element in a list 
l.insert(2,34) # if you want to insert an element in list first place decide where to insert index and next place is what to insert
m = l.copy() # if you want to copy same but different name
l.extend(m) # if add the elements of m at end of l list
k = l + m # if you dont want to change l
print(l)
