price = int(input())
if price >= 300:
    percentage = (30 / 100) * price
    price = (price - percentage)

elif price < 300 and price >= 200:
    percentage = (20 / 100) * price
    price = (price - percentage)
    
elif price < 200 and price >= 100:
    percentage = (10 / 100) * price
    price = (price - percentage)
    
elif price < 100 and price > 0:
    percentage = (5 / 100) * price
    price = (price - percentage)

elif price <= 0:
    percentage = 0
    price = (price - percentage)
        
print(price)    
     
'''price = 250

if price >= 300:
    price *= 0.7  # (1 - 0.3)
elif price >= 200:
    price *= 0.8  # (1 - 0.2)
elif price >= 100:
    price *= 0.9  # (1 - 0.1)
elif price < 100 and price >= 0:
    price *= 0.95  # (1 - 0.05)

print(price)
price * (1 - discount)'''        