sea_excursion_amount = int(input())
mountain_excursion_amount = int(input())
command = ""
price_for_sea = 680
price_for_mountain = 499
profit = 0
while command != "Stop":
    command = input()
    if command == "sea" and sea_excursion_amount >= 1:
        sea_excursion_amount -= 1
        profit += price_for_sea
    elif command == "mountain" and mountain_excursion_amount >= 1:
        mountain_excursion_amount -= 1
        profit += price_for_mountain
    if sea_excursion_amount == 0 and mountain_excursion_amount == 0:
        break
if sea_excursion_amount == 0 and mountain_excursion_amount == 0:
    print(f"Good job! Everything is sold.")
print(f"Profit: {profit} leva.")
