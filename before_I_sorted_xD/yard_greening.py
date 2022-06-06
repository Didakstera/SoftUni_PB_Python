price_for_square_meter = 7.61
total_square_meters = float(input())
total_price = price_for_square_meter * total_square_meters
final_price = total_price * 0.82
discount = total_price - final_price
print(f"The final price is {final_price}")
print(f"The discount is {discount}")