money_in = 0
text = "Increase:"
while text != "Invalid operation!":
    command = input()
    if command == "NoMoreMoney":
        break
    deposit = float(command)
    if deposit < 0:
        text = "Invalid operation!"
        print(text)
        break
    money_in += deposit
    print(f"{text} {deposit:.2f}")

print(f"Total: {money_in:.2f}")
