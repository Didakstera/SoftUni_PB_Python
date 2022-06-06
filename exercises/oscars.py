actor_name = input()
academy_starting_points = float(input())
jury_amount = int(input())
all_points = 0 + academy_starting_points

for people in range(1, jury_amount + 1):
    jury_points_for_letters = 0
    jury_name = input()
    new_points = float(input())
    for char in range(len(jury_name)):
        jury_points_for_letters += 1
    all_points += ((new_points * jury_points_for_letters) / 2)
    if all_points > 1250.5:
        break
if all_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {all_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {(1250.5 - all_points):.1f} more!")
