"""
Local variables are the variables that declared inside the function and have scope within the function. 

When there is no class created and a variable is created directly in file then it is a global variable.
To access the global variable inside a function we use global keyword.

"""
""" Below we see an example of local variable"""
def sum(x,y):
    sum = x + y
    return sum

print(sum(5, 10))
