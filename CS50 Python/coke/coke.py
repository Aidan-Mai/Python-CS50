price = 50

while price > 0:
    print('Amount Due:', price)
    Coin = int(input('Insert Coin: '))
    if Coin in [25, 5, 10]:
        price -= Coin

change = abs(price)
print('Change Owed: ',change)

