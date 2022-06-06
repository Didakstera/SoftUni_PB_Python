month = input()
days_booked = int(input())
studio_price = 0
apartment_price = 0
discount_apartment = 0
discount_studio = 0
if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if 7 < days_booked <= 14:
        discount_studio = 0.05
    elif days_booked > 14:
        discount_apartment = 0.10
        discount_studio = 0.30
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if days_booked > 14:
        discount_studio = 0.20
        discount_apartment = 0.10
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
    if days_booked > 14:
        discount_apartment = 0.10
studio_price_with_discount = (studio_price - studio_price * discount_studio) * days_booked
apartment_price_with_discount = (apartment_price - apartment_price * discount_apartment) * days_booked
print(f"Apartment: {apartment_price_with_discount:.2f} lv.")
print(f"Studio: {studio_price_with_discount:.2f} lv.")
