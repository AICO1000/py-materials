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
# Function Creation - def function_name(parameters): body
def print_function ():
    print("This")
    print("is")
    print("A")
    print("function")
    
print_function()
print_function()    

# Functions with parameters - meaning passing data into the functions.
# The actual value/variable passed into the parameter are known arguments
def minimum(first, second):
    if (first < second):
        print(first)
    else:
        print(second)
        
num1 = 10
num2 = 20

minimum(num1, num2)            

# return statement
def minimum(first,second):
    if (first < second):
        return first
    return second

num1 = 20
num2 = 30
result = minimum(num1, num2)

print(result)

'''It is a good practice to define all our functions first and then begin the main code. Defining them first ensures that they can be used anywhere in the program safely.'''

# Function Scopes = Function body
# Data Lifecycle - Data crated inside the function can not used outside on less it is begin return by the function.
#example - below code will never code
'''def func():
    name = "Sam"
func()
print(name)    
'''
# Also function cannot access code outside it's scope except it is passed as an argument
name = "Ned"

def func():
    name = "sam"
    
func()
print(name)    # The value doesn't change

'''When a mutable data is passed to a function the function can modify and edit it with the modifications staying effective outside the function scope, e.g. list.
When an immutable data is passed to a function the function can modify and edit it without the modification not begining effective outside the function scope, e.g integers, strings. '''
#immutable
num = 20

def multiply_by_10(n):
    n *= 10
    num = n
    print("Value of num inside the function %i" % num)
    return n

multiply_by_10(num)
print("Value of num outside the function", num)

# mutable
num_list = [10, 20, 30, 40]
print(num_list)

def multiply_by_10(my_list):
    my_list[0] *= 10
    my_list[1] *= 10
    my_list[2] *= 10
    my_list[3] *= 10
    
multiply_by_10(num_list)
print(num_list)  

# Built-in string function  
# Functions that are properties of a particular entity are known as method. These methods can be accessed with the .opearator.
# Search 
# find()-a_string.find(substring, start, end), start and end are optional
random_string = "This is a string"
print(random_string.find("is"))
print(random_string.find("is", 9, 13))

# Replace() - can be used to replace a part of a string with another striing
# a_string.replace(string_to_be_replaced, new_string)
a_string = "Welcome to Deenation"
print(a_string.replace("Welcome to", "Greetings from"))

# Changing the letter case
print("UpperCase".upper())
print("LowerCase".lower())

# Joining - with join() method we can join multiple strings together
llist = ["a", "b", 'c']
print('>>'.join(llist))
print('<<'.join(llist))
print(', '.join(llist))

# Formatting - The format() can be used to format specified values and insert them in string's placeholders
# The placeholders can be identified by a named indexed{cname}, numbered indexes{0}, or even an empty placeholder{}.
string1 = "Learn Python {version} at {cname}".format(version = 3, cname = "Aicocademy")
string2 = "Learn Python {0} at {1}".format(3, "Aicocademy")
string3 = "Learn Python {} at {}".format(3, "Aicocademy")
print(string1)
print(string2)
print(string3)

'''Type conversion - In python sometimes we want to change data type of a data'''
# int() - changes the data to an integer. strings can only be changed to an integer if it contents numbers
print(int("20"))
print(int(20.5))
print(int(False))

# ord() -  This function can be used to convert a character to its unicode
print(ord('a'))
print(ord('0'))

# float() - The flaot() function translate data to a floating point number
print(float(25))
print(float("23.8"))
print(float(True))

# str() - To convert data into string
print(str(20) + '2')
print(str(False))
print(str(12.789) + 'is a string')

# bool
print(bool(10))
print(bool(0.0))
print(bool("string"))
print(bool(False))

# The input() function - takes users input
# name = input("what is your name? ")
# print("\nHello", name)

'''lambdas - lambda
We have to specify function names while creating them. However, there is some special functions where we don't need to specify the function names.
Definition - A lamda is an anonymous function that returns some form of data'''
# syntax - lambda parameters: expression - parameters are option 
triple = lambda num : num * 3
print(triple(10))

string = lambda a, b, c : a[0] + b[0] + c[0]

print(string("World", "Wide", "Web"))
# A single line function for short function
# for conditional statement
temp = lambda num : 'high' if num > 10 else 'low'
print(temp(5))
print(temp(50)) 

'''Functions as Argurment'''
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
def calculator(operation, n1, n2):
    return operation(n1, n2)
result = calculator(add, 10, 20)
print(result)
print(calculator(multiply, 10, 20))

# Using lambdas
def calculator(operatiion, n1, n2):
    return operatiion(n1, n2)

result = calculator(lambda n1, n2 : n1 + n2, 10, 20)
print(result)

print(calculator(lambda n1, n2 : n1 * n2, 10, 50))

# map() - creates a map object from an existing list and a function as it's parameters. This object can be converted to a list by using the list() function
# templates - map(function, list)
num_list = [0,1,2,3,4,5]

double_list = map(lambda n: n * 3, num_list)

print(list(double_list))

# filters() - requires a function and list - it filters elements that are in a list if the element satify the condition
numList = [30, 2, -15, 17, 9, 100]

greater_than_10 = list(filter(lambda n: n > 10, numList))

print(greater_than_10)

'''Recursion - is when a function calls itself during execution'''
def rec_count(number):
    print(number)
    if number == 0:
        return 0
    rec_count(number - 1)
    print(number)
    
rec_count(5) 
'''Why use recursion
1. Reduce runtime of certain algorithms
2. Solves graph and trees related problem
3. Important in search alorithms
'''
def fac(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * fac(n -1)

print(fac(5))

# def factorial(n):
#     # Base case
#     if n == 0 or n == 1:
#         return 1

#     if n < 0:
#         return -1
#     # Recursive call
#     return n * factorial(n - 1)


# print(factorial(5))