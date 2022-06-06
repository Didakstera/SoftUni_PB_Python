group_budget = int(input())
season = input()
fisherman_count = int(input())
ship_rent_cost = 0
discount = 0
additional_discount = 0
if season == "Spring":
    ship_rent_cost = 3000
elif season == "Summer" or season == "Autumn":
    ship_rent_cost = 4200
elif season == "Winter":
    ship_rent_cost = 2600
if fisherman_count <= 6:
    discount = ship_rent_cost * 0.1
elif 7 <= fisherman_count <= 11:
    discount = ship_rent_cost * 0.15
elif 12 <= fisherman_count:
    discount = ship_rent_cost * 0.25
final_price_one = ship_rent_cost - discount
if season == "Spring" or season == "Summer" or season == "Winter":
    if fisherman_count % 2 == 0:
        additional_discount = final_price_one * 0.05
final_price = final_price_one - additional_discount
if group_budget >= final_price:
    print(f"Yes! You have {(group_budget - final_price):.2f} leva left.")
if group_budget < final_price:
    print(f"Not enough money! You need {(final_price - group_budget):.2f} leva.")
