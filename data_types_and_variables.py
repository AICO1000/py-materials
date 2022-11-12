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
str1 = "Hello"
print(id(str1))

str1 = "world"
print(id(str1))

num = 345
print(int(num[0]))

