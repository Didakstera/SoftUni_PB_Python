lilys_age = int(input())
washer_price = float(input())
price_for_a_toy = int(input())
toys = 0
money = 10
sum_money = 0
for odd_birthdays in range(1, lilys_age + 1, 2):
    toys += 1
for even_birthdays in range(2, lilys_age + 1, 2):
    sum_money += money
    money += 10
toys_money = toys * price_for_a_toy
if lilys_age % 2 == 0:
    brother_steals = lilys_age / 2
else:
    brother_steals = (lilys_age - 1) / 2
all_money_lily_has = sum_money + toys_money - brother_steals
if all_money_lily_has >= washer_price:
    print(f"Yes! {(all_money_lily_has - washer_price):.2f}")
else:
    print(f"No! {(washer_price - all_money_lily_has):.2f}")
