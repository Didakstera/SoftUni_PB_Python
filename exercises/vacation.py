money_required = float(input())
starting_money = float(input())
days_passed = 0
consecutive_spending = 0
while money_required > starting_money:
    action = input()
    money = float(input())
    days_passed += 1
    if action == "spend":
        if money < starting_money:
            starting_money -= money
        else:
            starting_money = 0
        consecutive_spending += 1
    elif action == "save":
        starting_money += money
        consecutive_spending = 0
    if consecutive_spending == 5:
        break
if consecutive_spending == 5:
    print(f"You can't save the money.")
    print(days_passed)
else:
    print(f"You saved the money for {days_passed} days.")
