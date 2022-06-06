number_1 = int(input())
counter = 1
is_counter_bigger = False
for row in range(1, number_1 + 1):
    for numbers in range(1, row + 1):
        if counter > number_1:
            is_counter_bigger = True
            break
        print(str(counter) + " ", end="")
        counter += 1
    if is_counter_bigger:
        break
    print()
