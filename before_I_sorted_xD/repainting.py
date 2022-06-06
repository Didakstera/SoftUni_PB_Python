protective_nylon = 1.5
paint = 14.5
paint_thinner = 5
bags = 0.4
nylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
work_hours_needed = int(input())
bonus_nylon = 3
bonus_paint = paint_needed / 10
nylon_price = protective_nylon * nylon_needed + bonus_nylon
paint_price = paint * paint_needed + bonus_paint * 14.5
thinner_price = paint_thinner * thinner_needed
materials_price = nylon_price + paint_price + thinner_price + bags
work_hours_price = materials_price * 0.3 * work_hours_needed
all_costs_price = work_hours_price + materials_price
print(all_costs_price)

