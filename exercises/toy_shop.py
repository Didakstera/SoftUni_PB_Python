price_for_trip = float(input())
puzzle_amount = int(input())
talking_doll_amount = int(input())
teddy_bear_amount = int(input())
minion_amount = int(input())
truck_amount = int(input())
rent = 10/100
puzzle_price = 2.60
talking_doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2
all_toys_sold = puzzle_amount + talking_doll_amount + teddy_bear_amount + minion_amount + truck_amount
all_toys_sold_price = puzzle_amount * puzzle_price + talking_doll_amount * talking_doll_price + \
                teddy_bear_amount * teddy_bear_price + minion_amount * minion_price + truck_amount * truck_price
if all_toys_sold >= 50:
    all_toys_sold_price = all_toys_sold_price - all_toys_sold_price * 0.25
money_for_trip = all_toys_sold_price - all_toys_sold_price * rent
if money_for_trip >= price_for_trip:
    print(f"Yes! {(money_for_trip - price_for_trip):.2f} lv left.")
else:
    print(f"Not enough money! {(price_for_trip - money_for_trip):.2f} lv needed.")
