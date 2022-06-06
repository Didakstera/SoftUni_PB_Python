deposit_amount = float(input())
deposit_term = int(input())
annual_interest_rate = float(input())
annual_deposit_reward = deposit_amount * annual_interest_rate / 100
monthly_deposit_reward = annual_deposit_reward / 12
deposit_reward = deposit_amount + deposit_term * monthly_deposit_reward
print(deposit_reward)
