amount_numbers = int(input())
first_numbers = 0
second_numbers = 0
third_numbers = 0
fourth_numbers = 0
fifth_numbers = 0
for numbers in range(1, amount_numbers + 1):
    number = int(input())
    if number < 200:
        first_numbers += 1
    elif 200 <= number < 400:
        second_numbers += 1
    elif 400 <= number < 600:
        third_numbers += 1
    elif 600 <= number < 800:
        fourth_numbers += 1
    elif number >= 800:
        fifth_numbers += 1
percent_1 = first_numbers / amount_numbers * 100
percent_2 = second_numbers / amount_numbers * 100
percent_3 = third_numbers / amount_numbers * 100
percent_4 = fourth_numbers / amount_numbers * 100
percent_5 = fifth_numbers / amount_numbers * 100
print(f"{percent_1:.2f}%")
print(f"{percent_2:.2f}%")
print(f"{percent_3:.2f}%")
print(f"{percent_4:.2f}%")
print(f"{percent_5:.2f}%")
