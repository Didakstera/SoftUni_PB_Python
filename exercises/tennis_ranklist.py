import math
tournaments_attended = int(input())
starting_points = int(input())
won_points = 0
won_tournaments = 0
for tournaments in range(1, tournaments_attended + 1):
    phase_reached = input()
    if phase_reached == "W":
        won_points += 2000
        won_tournaments += 1
    elif phase_reached == "F":
        won_points += 1200
    elif phase_reached == "SF":
        won_points += 720
final_points = won_points + starting_points
average_points = won_points / tournaments_attended
percent_won_tournaments = won_tournaments / tournaments_attended * 100
print(f"Final points: {final_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{percent_won_tournaments:.2f}%")
