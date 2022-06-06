number_1 = int(input())
number_2 = int(input())
operator = input()
sum = 0
even = True
if operator == "+":
    sum = number_1 + number_2
elif operator == "-":
    sum = number_1 - number_2
elif operator == "*":
    sum = number_1 * number_2
elif operator == "/" and number_2 != 0:
    sum = number_1 / number_2
elif operator == "%" and number_2 != 0:
    sum = number_1 % number_2
if operator == "+" or operator == "-" or operator == "*":
    if sum % 2 == 1:
        even = False
if operator == "/" and number_2 == 0 or operator == "%" and number_2 == 0:
    print(f"Cannot divide {number_1} by zero")
elif operator == "/":
    print(f"{number_1} {operator} {number_2} = {sum:.2f}")
elif operator == "%":
    print(f"{number_1} {operator} {number_2} = {sum}")
elif even != True:
    print(f"{number_1} {operator} {number_2} = {sum} - odd")
else:
    print(f"{number_1} {operator} {number_2} = {sum} - even")
