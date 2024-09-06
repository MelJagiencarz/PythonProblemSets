amount_due = 50

while amount_due > 0:
    print(f'Amount Due: {amount_due}')
    coin = input('Insert Coin: ')
    if int(coin) < 30:
        amount_due -= int(coin)

if amount_due < 0:
    amount_due *= -1

print(f'Change Owed: {amount_due}')

