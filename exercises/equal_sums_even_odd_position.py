first_number = int(input())
second_number = int(input())
for number in range(first_number, second_number + 1):
    number_to_str = str(number)
    even_sum = 0
    odd_sum = 0
    for number_2 in range(0, len(number_to_str)):
        digit = int(number_to_str[number_2])
        if number_2 % 2 == 0:
            even_sum = even_sum + digit
        else:
            odd_sum = odd_sum + digit
    if even_sum == odd_sum:
        print(number_to_str, end=" ")
