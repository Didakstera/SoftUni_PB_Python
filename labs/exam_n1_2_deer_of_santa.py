import math
days_santa_is_missing = int(input())
food_santa_has_left = int(input())
first_deer_food_daily = float(input())
second_deer_food_daily = float(input())
third_deer_food_daily = float(input())
first_deer_ate_total = days_santa_is_missing * first_deer_food_daily
second_deer_ate_total = days_santa_is_missing * second_deer_food_daily
third_deer_ate_total = days_santa_is_missing * third_deer_food_daily
all_food_needed = first_deer_ate_total + second_deer_ate_total + third_deer_ate_total
if food_santa_has_left >= all_food_needed:
    food_left = food_santa_has_left - all_food_needed
    print(f"{math.floor(food_left)} kilos of food left.")
else:
    food_missing = all_food_needed - food_santa_has_left
    print(f"{math.ceil(food_missing)} more kilos of food are needed.")
