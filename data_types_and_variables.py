# Data Types and Variables
# Data Type of an item is the type and range of values the item can occupy

# Numbers - Integers, Floating point numbers, Complex numbers.
# Integers are positive and negetive whole numbers.
# Exmaples of integers
print(10) # A positive integer 
print(-3000) # A negetive integer

num = 1234 # Assinging an integer to a variable
print(num)
num = -234 # Assigning a new integer
print(num)

# Floating point numbers or floats are postive and negetive decimal numbers.
# Examples of floats
print(0.002) # A positive float
print(-32.954) # A negetive float

floats_numbers = 3.124 # Assigning a variable to flaot
print(floats_numbers)
floats_numbers = -4345.95
print(floats_numbers)

# Complex numbers comprises of a real and imaginary number and it is created by using complex(real, imaginary)
#Examples of complex numbers
print(complex(50, 10)) # Represents (50 + 10j) complex number
print(complex(2.5, -30)) # Repesent (2.5 - 30j) complex number

complex_number1 = complex(0,3)
print(complex_number1)
complex_number2 = complex(3, 0)
print(complex_number2)

# Boolean also known as bool allows you to choose between two value: True and False
print(True)
boolean_value = False # Assigning variable to bool
print(boolean_value)

# Strings can be a single character or entirely empty
print("How to get away with murder!") # Double quoated
got = 'Game of thrones.......' # Single quoated
print(got)
print("$") # Single character

empty = "" # An empty line
print(empty)

multiple_lines = '''Triples'''
print(multiple_lines)

# length of a string is found by using the len() built-in function. The len() function indicates the number of character in the string.
string_length = "I am human being"
print(len(string_length))

# Indexing is a string every character is given a index numerical based on position n-1
# Accesing string - Each character in a string can be accessed using index. [index number]
index = "Bruce Wayne"

first = index[0] # Accesing the first character 
print(first)

space = index[5] # Accessing the empty space in the string
print(space)

last = index[len(index) - 1] # Accessing the last character in the string.
print(last)

# Reverse indexing is done by using negetive indices. which starts from the last of the character in the string that is represented by -1
print(index[-1]) # Corresponds to index[10]
print(index[-5]) # Cooresponds to index[6]

# String Immutability: Once we assign a value to a string we can not update it - When we assign a new value to a variable it only change it's identity not the value.
# Python doesn't support item assignment in case of string.
''' python = "Immutability"
    python[0] = "O" '''

str1 = "Hello"
print(id(str1))

str1 = "world"
print(id(str1))

# ASCII vs Unicode
'''python3 uses unicode but the older version python2.x use the ASCII and to use a unicode string the u must be in front of the string'''
unicode = u'An example of ASCII using unicode'

# NoneType has a single value "None" we can assign None to a variable but we can not create other variable NoneType
val = None
print(val)
print(type(val))

'''None is not 0
   None is not the same as False
   None is not an empty string
   None is not the value of a variable that has not be assigned a value'''

# String slicing is a process of obtaining a portion(substring) of string by using it's index- string[start:end]
# Note the end index in the substring will not appear
my_string = "This is MY String!"
print(my_string[0:4])
print(my_string[1:7])
print(my_string[8:len(my_string)])

# Step slicing - python3 allows us to slice a string by which we can skip characters in the string
# The default step is 1
print(my_string[0:7:2])
print(my_string[0:7:3])
print(my_string[3:len(my_string):3])

# Reverse slicing - We can also decide to return the reserve of a substring
# This will be done by us switching the "start" and "end" position
print(my_string[13:2:-1])
print(my_string[13:2:-2])

# Partial slicing - it is optional to indicate the start and end indicies
# if the start is given but the end is not given 
# if the end is given but the start is not given
print(my_string[:8])
print(my_string[3:])
print(my_string[:]) # returns all the characters in the string
print(my_string[::-1]) # reserve slice 

'''String Formatting - means substituting values into a string
1. Inserting strings into strings
2. Inserting integers into strings
3. Inserting floats into strings'''
# 1. Inserting strings within a string
print("I love %s" % "Python")
temp = "Educative"
print("I love %s " % temp)
print("I love %s and %s" % ("Python",temp)) # The %s format specifier tells python to insert strings. 

# 2. Inserting Integer within a string
my_string = "%i + %i = %i " % (1,2,3) # The %i format specifier tells python to insert integers here.
print(my_string)

# 3. Inserting Float within a strings
my_string1 = "%f" % (1.11)
print(my_string1)  # outputs the floatting number 

my_string2 = "%.3f" % (1.11)
print(my_string2) # outputs the floatting number in 3 decimal place

my_string3 = "%.2f" % (1.117)
print(my_string3) # rounds up the floatting number in 2 decimal place 

''' Operators - are used to perform arithmetic and logic operations on data. They enable us to manipulate and interpret data to produce useful outputs
Operators are represented by characters or special keywords
In-fix - the operators appear in between two operands which the two operands act upon and it is known as binary operators (operand)(operator)(operand)
prefix - the operators appear in front of the operands which is known as unary operators (operator)(operand)
types of operators are:
arithmetic operators
logical operators
comparison operators
assignment operators
bitwise operators'''

# Arithmetic operators 
'''arithmetic operators in order of precedence
(), **, (%, *, /, //), (+, -)'''

# Addition
print(10 + 5)

float1 = 13.65
float2 = 3.40
print(float1 + float2)

num = 20
flt = 3.409799
print(num + flt)

# Subtraction - we can subtract a number from another by using the ( - ) operator
print(10 - 5)

float1 = -18.678
float2 = 3.55
print(float1 - float2)

num = 20
flt = 10.5
print(num - flt)

# Division - we can divide a number from another by using the ( / ) operator
# A division operator always results to a floating point number
print(40 / 10)

float1 = 5.5
float2 = 4.5
print(float1 / float2)
print(12.4 / 2)

# Floor Division - in floor division the results is always floored in the nearest integer. it is also known as integer divison. 
# For the floor division we must use the // operator. 
print(43 // 10)

float1 = 5.5 
float2 = 4.5
print(float1 // float2)
print(12.4 // 2)

# Modulo - A number's modulo with another number is found by using the % operator
print(10 % 2)

twenty_eight = 28
print(twenty_eight % 10)

print(-28 % 10) # The remainder will be positive if the right-hand operand is positive
print(28 % -10) # The remainder will be negetive if the right-hand operand is negetive
print(34.4 % 2.5) # The remainder can be a float

# Precedence - an arithmetic expression with different operators will be computed based on their operator precedence.
# Whenever operators have equal precedence the expression is computed from the left side.
print(10 - 3 * 2) # (*) first followed by (-)
print(3 * 20 / 5) # same precedence
print(3 / 20 * 5) # same precedence 

# Parentheses - An expression with parentheses will be computed first regardless of the operator precedence.
print((10 - 3 ) * 2)
print((18 + 2) / (10 % 8))

'''Comparision Operators - can be used to compare values in mathematical terms
<, >, >=, <=, ==, !=, is, is not
Comparison is always a bool
If the result of the comparison is correct the results is True otherwise it is False.
The == and != operators compare values of both operands. However, the identity operators, is and is not, check whether the two operands are exact same object'''
num1 = 5
num2 = 10
num3 = 10
list1 = [6,7,8]
list2 = [6,7,8]

print(num2 > num1)
print(num1 > num2)

print(num2 == num3)
print(num3 != num1)
print(3 + 10 == 5 + 5)
print(3 <= 2)

print(num2 is not num3)
print(list1 is list2)

'''Assignment operator - in this category the operator assign value to a variable. The "=" operator is used to assign values but it is not the only one.
=, +=, -=, *=, /=, //=, **=, |=, &=, ^=, >>=, <<=
Assigning Values - Variables are mutable so we change their values anytime'''

year = 2019
print(year)

year = 2020
print(year)

year = year + 1
print(year)

first = 12
second = first
first = 24 # updating first

print(first, second) # second remains unchanged

# The other operators
num = 10
print(num)

num += 5
print(num)

num -= 5
print(num)

num *= 2
print(num)

num /= 2
print(num)

num **= 2
print(num)

num //= 24
print(num)

'''Logical operators are used to manipulate the logic of boolean expression
OR, AND, NOT
Logical expression are formed by using logical and boolean operators'''

my_bool = True or False
print(my_bool)

my_bool = True and False 
print(my_bool)

my_bool = False
print(not my_bool)

# Bit Values True = 1, False = 0
# Python automatically changes the bool to numerical values

print(10 *  True)
print(10 * False)

# Bitwise - all data are made up of 0s and 1s known as bits. Bitwise operators allow us to perform bit-related operations on value
num1 = 10 # binary 01010
num2 = 20 # binary 10100

print(num1 & num2) # 0 --> 01010 x 10100 = 00000
print(num1 | num2) # 30 --> 01010 + 10100 = 11110
print(~num1) # -11
print(num1 ^ num2) # 30 --> 11110
print(num2 >> 3) # 2 --> 00010
print(num1 << 3) # 80 --> 0101 0000

'''String operation
Comparison operations - strings are compatible with comparison operators. Each character has a unicode value.
This allows strings to be compared on the basis of their unicode values'''

print("a" < "b") # a has a smaller unicode value

house = "Gryffindor"
house_copy = "Gryffindor"

print(house == house_copy)

new_house = "Slytherin"
print(house == new_house)
print(new_house <= house)
print(new_house >= house)

# Concatenation
# The + operator can be used to merge two strings together

first_name = "Samuel"
last_name = "Adamu"
full_name = first_name + last_name
print(full_name)

# The * operator allows us to multiply strings in repeating pattern
print("ha" * 3)

# Search
# The "in" keyword can be used to check if a particular substring exists in another string. If the substring is found it returns true
random_string = "This is a random string"
print('of' in random_string) 
print('random' in random_string)

# Grouping values - we can group various values together in one variable but the most popular is the list. it is similar to a string since a string is a collection of characters the lsit is a collection of values of different types. by using [] and seperating them with comma.
# Making a list
my_list = [1, 2.5, "A string", True]
print(my_list)
print(my_list[2]) # can be indexed and sliced like strings
print(len(my_list)) # the len works with them too 

