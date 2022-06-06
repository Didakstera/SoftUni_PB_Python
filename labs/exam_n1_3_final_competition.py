dancers_count = int(input())
points_amount = float(input())
season = input()
location = input()
money_prize = 0
if location == "Abroad":
    money_prize = points_amount * dancers_count + ((points_amount * dancers_count) * 0.5)
    if season == "summer":
        money_prize -= money_prize * 0.1
    elif season == "winter":
        money_prize -= money_prize * 0.15
elif location == "Bulgaria":
    money_prize = points_amount * dancers_count
    if season == "summer":
        money_prize -= money_prize * 0.05
    elif season == "winter":
        money_prize -= money_prize * 0.08
donation_amount = money_prize * 0.75
money_prize_after_donation = money_prize - donation_amount
money_per_dancer = money_prize_after_donation / dancers_count
print(f"Charity - {donation_amount:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")
