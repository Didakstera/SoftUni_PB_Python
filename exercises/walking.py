steps_goal = 10000
steps_today = 0
steps_for_a_walk = ""
last_steps = 0
while steps_for_a_walk != "Going home":
    steps_for_a_walk = input()
    if steps_for_a_walk != "Going home":
        steps_today += int(steps_for_a_walk)
    else:
        last_steps = int(input())
        steps_today += last_steps
    if steps_today > steps_goal:
        break
if steps_today >= steps_goal:
    print("Goal reached! Good job!")
    print(f"{steps_today - steps_goal} steps over the goal!")
else:
    print(f"{steps_goal - steps_today} more steps to reach goal.")
