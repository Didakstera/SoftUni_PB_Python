flower_type = input()
amount_flowers = int(input())
budget = int(input())
flowers_price = 0
roses_cost = 5
dahlias_cost = 3.80
tulips_cost = 2.80
narcissus_cost = 3
gladiolus_cost = 2.50
if flower_type == "Roses":
    flowers_price = amount_flowers * 5
    if amount_flowers > 80:
        flowers_price = flowers_price - flowers_price * 0.1
elif flower_type == "Dahlias":
    flowers_price = amount_flowers * 3.80
    if amount_flowers > 90:
        flowers_price = flowers_price - flowers_price * 0.15
elif flower_type == "Tulips":
    flowers_price = amount_flowers * 2.80
    if amount_flowers > 80:
        flowers_price = flowers_price - flowers_price * 0.15
elif flower_type == "Narcissus":
    flowers_price = amount_flowers * 3
    if amount_flowers < 120:
        flowers_price = flowers_price + flowers_price * 0.15
elif flower_type == "Gladiolus":
    flowers_price = amount_flowers * 2.50
    if amount_flowers < 80:
        flowers_price = flowers_price + flowers_price * 0.20
if flowers_price <= budget:
    print(f"Hey, you have a great garden with {amount_flowers} {flower_type} and {(budget - flowers_price):.2f} leva left.")
elif budget < flowers_price:
    print(f"Not enough money, you need {(flowers_price - budget):.2f} leva more.")
