floors_amount = int(input())
rooms_amount = int(input())
floor_letter = ""
for current_floor in range(floors_amount, 0, - 1):
    for current_room in range(0, rooms_amount):
        if current_floor == floors_amount:
            floor_letter = "L"
        elif current_floor % 2 == 0:
            floor_letter = "O"
        else:
            floor_letter = "A"
        print(f"{floor_letter}{current_floor}{current_room}", end=" ")
    print()
