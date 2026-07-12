# operations on Tuples in python 
# tuples are immutable and lists are mutable

# we directly cant change tuple so we should convert it into list first then change
tup = (2,4,5,"bhal","bheem")
temp = list(tup)
temp.append("rohit")
temp.pop(3)
temp[2] = 10
tup = tuple(temp)
print(tup)

countries = ("pakistan","afganistan","bangladesh")
countries2 = ("india","vietnam","india")
SouthEastAsia = countries + countries2
print(SouthEastAsia)


tuple = (2,4,5,7,5,1,2,3,7,9,6,4,5,3,2,5,7,9,7,4,)
print(tuple.count(5))
print(tuple.index(5,1,7))# here 1st element is specified element and 0ther 2 are index range
