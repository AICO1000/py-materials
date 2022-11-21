''' Function
A function is reusable set of operations
print() and len() perform predefined task so we can they're examples of functions
# Reusability and simplicity are the primary reasons to use functions'''
# An input isn't even necessary. A function could perform it's own computations to complete a task.
num1 = 10
num2 = 20
if num1 < num2:
    minimum = num1
else:
    minimum = num2
print(minimum)        

num1 = 250
num2 = 150
if num1 < num2:
    minimum = num1
else:
    minimum = num2
print(minimum)    

# For every pair of integers we need to write the if-else statement over again      
# The good news is that python already has the min function

minimum = min(10, 40)
print(minimum)

minimum = min(10, 100, 1, 1000)
print(minimum)

minimum = min("Superman", "Batman")
print(minimum)

'''Types of functions
1. built-in functions
2. User-defined functions
print(), len() and min() are examples of built-in functions'''
# Python allows us to create our own functions that perform tasks we require.