# Doc strings and PEP8

def square(n):
    '''Takes in a number n , returns
thesquare of n'''      # this is not comment
    print(n**2)
square(5)

print(square.__doc__)

# Python Enhancement Proposal 8 (PEP8)

''' it is Python's official style guide—a set of rules for writing 
clean, readable, and consistent Python code.'''

# zen of code 

# its a poem written by Tim peters 

'''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''