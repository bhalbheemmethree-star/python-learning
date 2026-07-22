# Finally keyword in python

try:
    l = [1,3,5,2]
    i = int(input("Enter the Index: "))
    print(l[i])
except:
    print("Some error occurred")
finally:
    print("I am always executed")

# this finally keyword is always executed but not in while defining finctions

def fun1():
    try:
        l = [1,3,5,2]
        i = int(input("Enter the Index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0
    finally:
        print("I am always executed")


print(fun1())