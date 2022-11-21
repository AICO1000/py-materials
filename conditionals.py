# COnditional statements
# Conditional statements are boolean expression if True executes this piece of code. 
# It allows programs to branch out into different paths based on the boolean expressions result in True or False outcome
# In this way the conditional statements controls the flow of the code and allows the computer to think. Hence are classified as control structures.
# Conditional statements in python

'''if condtional statement is True:
    # execute expression1
    pass
else:
    # execute expression2
    pass

There are three types of conditional statements in python
1. if
2. if-else
3. if-elif-else    

if statement comprises of two part the condition and the code to be executed
if (condition):
    code to be executed

The : illustration specify the begining of if statement to be executed. the () in the condition is optional 

Indentation - plays an essential role in python. Statements with the the same level of indentation belong to the same block of code.'''

# The flow of the if statement- if the condition statement is True execute the code else skip and move on.

num = 5

if (num == 5):
    print("The number is equal to 5")   
    
if num > 5:
    print("The number is greater than 5")     
    
# Coditions with logical operators
num = 12
if num % 2 == 0 and num % 3 == 0 and num % 4 == 0:
    print("The number is a multiple of 2, 3, and 4")

if num % 5 == 0 or num % 6 == 0:
    print("The number is a multiple of 5 and/or 6")    
    
# Nested if statements - if statement inside another
num = 63

if num >= 0 and num <= 100:
    if num >= 50 and num <= 75:
        if num >= 60 and num <= 70:
            print("The number is in the 60-70 range")
# Each if statement has a further indentation            

# Creating and editing values - in conditional statement we can edit the values of the variable
num = 10
if num > 5:
    num = 20
    new_num = num * 5
        
print(num)
print(new_num)

# if-else statements - what if we want to execute a different set of operation when the case if is not True but False that's where if-else comes in
# Structure
num = 60 

if num <= 50:
    print("The number is less than or equal to 50")
else:
    print("The number is greater than 50")    

# Conditional Expression - it returns an output based on the condition we provide. The output can be stored in a variable.
# output_value1 if condition else output_value2
num = 60
output = "The number is less than or equal to 50" \
    if num <= 50 else "The number is greater than 50" # The backslash is a line contiuation character. That is used to slipt single line into multiple line.
print(output)

# if-elif-else statement - used for multiple conditions
# Structure - the if and else statement will stand while the elif statement come between them
light = "Yellow"

if light == "Green":
    print("Go")
    
elif light == "Yellow":
    print("Caution")
    
elif light == "Red":
    print("Stop")
    
else:
    print("Incorrect light signal")        
    
# Multiple elif statements - We can have many elif's statement as long it is they are between the if and else statement 
# An elif statement can stand without an elif statement at the end, but can not do without an if statement at the begining
num = 5 

if num == 0:
    print("Zero")
elif num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3:
    print("Three")
elif num == 4:
    print("Four")
elif num == 5:
    print("Five")
elif num == 6:
    print("Six")
elif num == 7:
    print("Seven")
elif num == 8:
    print("Eight")
elif num == 9:
    print("Nine")