change = float(input())
coin = round(change * 100)
amount_coins = 0
while coin != 0:
    if coin >= 200:
        coin -= 200
        amount_coins += 1
    elif coin >= 100:
        coin -= 100
        amount_coins += 1
    elif coin >= 50:
        coin -= 50
        amount_coins += 1
    elif coin >= 20:
        coin -= 20
        amount_coins += 1
    elif coin >= 10:
        coin -= 10
        amount_coins += 1
    elif coin >= 5:
        coin -= 5
        amount_coins += 1
    elif coin >= 2:
        coin -= 2
        amount_coins += 1
    elif coin >= 1:
        coin -= 1
        amount_coins += 1
print(amount_coins)