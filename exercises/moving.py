housing_width = int(input())
housing_length = int(input())
housing_height = int(input())
housing_capacity = housing_width * housing_height * housing_length
one_carrying = 0
boxes_sum = 0
while housing_capacity >= boxes_sum:
    one_carrying = input()
    if one_carrying == "Done":
        break
    else:
        boxes_sum += int(one_carrying)
if one_carrying == "Done":
    print(f"{housing_capacity - boxes_sum} Cubic meters left.")
else:
    print(f"No more free space! You need {boxes_sum - housing_capacity} Cubic meters more.")
