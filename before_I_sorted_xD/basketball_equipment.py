annual_price = int(input())
kicks_price = annual_price - annual_price * 0.4
jersey_price = kicks_price - kicks_price * 0.2
ball_price = jersey_price / 4
basketball_accessories = ball_price / 5
all_costs_annually = annual_price + kicks_price + jersey_price + ball_price + basketball_accessories
print(all_costs_annually)
