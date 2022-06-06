import sys

numbers_amount = int(input())
sum_numbers = 0
max_number = -sys.maxsize
for numbers in range(1, numbers_amount + 1):
      new_numbers = int(input())
      if new_numbers > max_number:
         max_number = new_numbers
      sum_numbers += new_numbers
if max_number == sum_numbers - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    sum_numbers -= max_number
    print(f"Diff = {abs(max_number - sum_numbers)}")
