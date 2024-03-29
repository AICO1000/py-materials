def fib(n):
    first = 0 
    second = 1
    
    if n <= 0:
        return -1
    
    if n == 1:
        return first
    
    if n == 2:
        return second
    
    count = 3
    while count <= n:
        fib_n = first + second
        first = second
        second = fib_n
        count += 1
    return fib_n
n = 8
print(fib(n))