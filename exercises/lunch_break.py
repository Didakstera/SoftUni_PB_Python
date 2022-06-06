import math
name_serial = input()
episode_duration = int(input())
break_duration = int(input())
time_to_eat = break_duration / 8
time_to_chill = break_duration / 4
time_left_for_watching = break_duration - (time_to_chill + time_to_eat)
if time_left_for_watching >= episode_duration:
    print(f"You have enough time to watch {name_serial} and left with {math.ceil(time_left_for_watching - episode_duration)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_serial}, you need {math.ceil(episode_duration - time_left_for_watching)} more minutes.")
