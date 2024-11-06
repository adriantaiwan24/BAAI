#
# Adrian
# Shopping Cart
#
 
i = 1
s = int(input("How many items do you want to buy? "))
total = 0
 
while (i <= s):
 
    # 1. Input
    name = input(f'Enter the name item {i}: ')
    price = int(input(f'Enter the price of {name}: ' ))
    quantity = int(input(f'Enter the quantity of {name}: ' ))
    sum1 = (price*quantity)
    print (f'Total cost for {name}: {sum1}')
    # 2. Process
    total += sum1
    i+=1  
       
# 3. Output
print(f'Total cost of your shopping cart: {total}')