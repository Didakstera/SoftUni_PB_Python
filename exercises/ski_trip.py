days_booked = int(input())
room_type = input()
comment = input()
nights_staying = days_booked - 1
price_for_a_night = 0
discount = 0
if room_type == "room for one person":
    price_for_a_night = 18
elif room_type == "apartment":
    price_for_a_night = 25
    if days_booked < 10:
        discount = 0.30
    elif 10 <= days_booked <= 15:
        discount = 0.35
    elif 15 < days_booked:
        discount = 0.50
elif room_type == "president apartment":
    price_for_a_night = 35
    if days_booked < 10:
        discount = 0.10
    elif 10 <= days_booked <= 15:
        discount = 0.15
    elif 15 < days_booked:
        discount = 0.20
price_before_comment = nights_staying * (price_for_a_night - price_for_a_night * discount)
if comment == "positive":
    final_price = price_before_comment + price_before_comment * 0.25
elif comment == "negative":
    final_price = price_before_comment - price_before_comment * 0.10
print(f"{final_price:.2f}")
