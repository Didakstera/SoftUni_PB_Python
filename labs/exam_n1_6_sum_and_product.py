number_n = int(input())
found_combination_1 = False
found_combination_2 = False
for number_a in range(1, 10):
    for number_b in range(9, number_a, -1):
        for number_c in range(10):
            for number_d in range(9, number_c, -1):
                sum_plus = number_a + number_b + number_c + number_d
                sum_multiplied = number_a * number_b * number_c * number_d
                if sum_plus == sum_multiplied and number_n % 10 == 5:
                    found_combination_1 = True
                    break
                elif sum_multiplied // sum_plus == 3 and number_n % 3 == 0:
                    found_combination_2 = True
                    break
                else:
                    continue
            if found_combination_1 or found_combination_2:
                break
        if found_combination_1 or found_combination_2:
            break
    if found_combination_1 or found_combination_2:
        break
if found_combination_1:
    print(f"{number_a}{number_b}{number_c}{number_d}")
elif found_combination_2:
    print(f"{number_d}{number_c}{number_b}{number_a}")
else:
    print("Nothing found")
