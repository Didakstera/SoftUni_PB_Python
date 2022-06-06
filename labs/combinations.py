number = int(input())
combinations_counter = 0
for first_number in range(0, number + 1):
    for second_number in range(0, number + 1):
        for third_number in range(0, number + 1):
            result = first_number + second_number + third_number
            if result == number:
                combinations_counter += 1
print(combinations_counter)
