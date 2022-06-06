film_budget = float(input())
statist_amount = int(input())
clothes_price_for_one = float(input())
decor_price = film_budget * 0.10
all_clothes_price = statist_amount * clothes_price_for_one
if statist_amount > 150:
    all_clothes_price = all_clothes_price - all_clothes_price * 0.10
if decor_price + all_clothes_price > film_budget:
    print("Not enough money!")
    print(f"Wingard needs {((decor_price + all_clothes_price) - film_budget):.2f} leva more.")
if decor_price + all_clothes_price <= film_budget:
    print("Action!")
    print(f"Wingard starts filming with {(film_budget - (decor_price + all_clothes_price)):.2f} leva left.")
