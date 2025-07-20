#price = int(input("Enter the price of the item: "))
price = int(input())

if price > 50000:
    # 20% discount
    price = price -  price * 0.2
elif 50000 > price > 20000:
    # 10% discount
    price = price -  price * 0.1
elif price < 20000:
    # No discount
    price = price

#print(f'The final price is: {price:.2f}')
#show final price integer
print(f'{price:.0f}')