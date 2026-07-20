# set methods in python

s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2)) # prints elements from both sets in order
s1.update(s2)  # this updates s1 by adding elements from s2
print(s1.intersection(s2)) # prints values common in both sets
print(s1.symmetric_difference(s2)) # prints uncommon elements
print(s1.difference(s2)) # this prints elements present in s1 but not in s2
print(s1.isdisjoint(s2)) # prints true if both sets are completely diff or prints false
print(s1.issuperset(s2)) # prints true if all elements of s2 are in s1 or prints false
print(s1.issubset(s2)) # prints true if s1 has values also present in s2
(s1.add(10)) # adds 10 to s1 set used only if to add only 1 element
s1.remove(1) # removes specific element from set shows error if specific element not in set
s1.remove(3) # same as remove but it doesnot show error anytime
s1.pop() # removes last element of set but set is unordered any element can be removed
del s1 # this deletes an entire set
s1.clear() # this deletes all items from set but not set

print(s1)
