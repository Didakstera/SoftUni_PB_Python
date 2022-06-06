budget = float(input())
season = input()
destination = "unknown"
place_to_stay = "unknown"
money_spent = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
      place_to_stay = "Camp"
      money_spent = budget * 0.3
    elif season == "winter":
      place_to_stay = "Hotel"
      money_spent = budget * 0.7
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
     place_to_stay = "Camp"
     money_spent = budget * 0.4
    elif season == "winter":
         place_to_stay = "Hotel"
         money_spent = budget * 0.8
elif budget > 1000:
      destination = "Europe"
      place_to_stay = "Hotel"
      money_spent = budget * 0.9
print(f"Somewhere in {destination}")
print(f"{place_to_stay} - {money_spent:.2f}")