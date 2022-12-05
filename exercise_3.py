def rep_cat(x ,y):
    x = str(x)
    y = str(y)
    return x * 10 + y * 5

result = rep_cat(4, 6)
print(result)

'''def rep_cat(x, y):
    return str(x) * 10 + str(y) * 5


print(rep_cat(3, 4))'''

def fac(n):
    if n == 1:
        return fac(n) * 1
    else:
        return fac(n) * fac(n -1)
    
fac(4)    
        