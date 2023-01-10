'''Loops are control structure that is used to perform a set of operation for a specify number of time
In python we have the 
1. while loop and
2. for loop
The for uses an iterator to transverse a sequence e.g range of numbers, an element of a list in simple terms the iterator is a variable that goes through the list.
The iterator starts from the beginning. In each iteration the iterator updates the next value of the sequence. The loop ends when it gets the end of the sequence'''
# Structure - The name of the iterator
           # The sequence to be transverse
           # The set of instruction to be performed
'''
for iterator in sequence :
        set of instructions to be performed
it always starts with a for keyword.
The in keyword specifies the iterator will go through the sequence or data structure
'''
# Looping through a range
'''The range() built-in function can be used to create a sequence of integers which a loop can iterate through the the list.
The format of the range: range(start, end, step)
The start is not specified as the default index is 0
The end index is not included 
The step is the number of step it should jump while iterating which is not necessary if you are not stepping the default is step 1'''

for i in range(1,11):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")
    # Using steps   
for i in range(1,11,3):
    print(i)            

# Looping through a list/string
float_number = [2.1,2.1,2.2,2.3]
print(float_number)
for i in range(0,len(float_number)):
    float_number[i] = float_number[i] * 2    
print(float_number)    

float_number = [2.5, 16.42, 10.77, 8.3, 34.21]
greater = 0
for num in float_number:
    if num > 10:
        greater += 1
print(greater)

# Nested 
'''The inner loop will always complete before the outer loop'''
# Executing nested for loop
n = 50
num_list = [10, 25, 4, 23, 6, 18, 27, 47]
for n1 in num_list:
    for n2 in num_list:
        if n1 != n2:
            if n1 + n2 == n:
                print(n1, n2)

                
# Break keyword - Sometimes we want to end a loop before it gets to the end. The break keyword helps us to break the loop whenever we want.
found = False
for n1 in num_list: # A bool that becomes true once a pair is found
    for n2 in num_list:
        if n1 != n2:
            if n1 + n2 == n:
                found = True    # Set found is True
                break # Break innner loop if the pair is found
    if found:
        print(n1, n2) # Print pair
        break # Break outer loop if a pair is found
    
# The continue keyword - The continue keyword helps in skipping the current iteration then moves to the next one.  
num_list = list(range(0,10))
for num in num_list:
    if num == 3 or num == 6 or num == 8:
        continue
    print(num)
    
# The keyword - helps to execute your program or code even when you have not written a set of code.
num_list = list(range(20))
if num in num_list:
    pass
print(len(num_list))    

# The break keyword
n = 10
x = 4
found = False
for i in range(0, n):
    if x == i + 1:
        found = True
        print("Number is found")
        break
else:
    print("Number not found")
    
# The continue keyword
for i in range(0, 10):
    if i%2 ==0:
        continue
    print(i)

# The while loop
'''The while loop keeps iterating over a certain set of operations as long as a certain condition holds True
it operates using the following logic:
while this condition is true, keep loop running'''

# Structure - while condition is true:
           # Loop over this set of operations
           
n = 2
power = 0
val = n
while val < 1000:
    power += 1
    val *= n
print(power)   

n = 249
last = n % 10
first = n
while first >= 10:
    first //= 10
result = first + last
print(result)  

'''Cautionary measures - compared to the for loop we must be very careful when creating a while loop. The while loop has the potential to never end which can trash the program
while(True):
    print("Hello World")

x = 1
while(x > 0):
    x += 5
    The above loop will never end because their reamain true
    
    OTHER PROPERTIES
    The break, conntinue and pass keyword works with while loop
    The while loop can be nested also
    We can also nest two types loops together
    '''
# Iteration vs. Recursion
# Recursion is useful when we need to divide data into different chunks.
# Iteration is useful for traversing data and also when we don't want the program's scope to change. 