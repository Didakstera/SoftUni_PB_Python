days_boiling = int(input())
rakia_degrees = 0
rakia_litres = 0
for work in range(1, days_boiling + 1):
    daily_rakiq = float(input())
    daily_degrees = float(input())
    rakia_litres += daily_rakiq
    rakia_degrees += daily_rakiq * daily_degrees

average_degrees_amount = rakia_degrees / rakia_litres
print(f"Liter: {rakia_litres:.2f}")
print(f"Degrees: {average_degrees_amount:.2f}")
if average_degrees_amount < 38:
    print(f"Not good, you should baking!")
elif 38 <= average_degrees_amount < 42:
    print(f"Super!")
else:
    print(f"Dilution with distilled water!")
