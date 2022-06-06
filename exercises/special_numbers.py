number = int(input())

for num_1 in range(1, 10):
    for num_2 in range(1, 10):
        for num_3 in range(1, 10):
            for num_4 in range(1, 10):
                if number % num_1 == 0 and number % num_2 == 0 and number % num_3 == 0 and number % num_4 == 0:
                    print(f"{num_1}{num_2}{num_3}{num_4}", end=" ")

