hours = int(input())
minutes = int(input())
if minutes >= 45 <= 59:
    hours = hours + 1
    minutes = minutes - 45
elif 0 <= minutes < 45:
    minutes = minutes + 15
if hours > 23:
    hours = 0
if 0 <= minutes <= 9:
 print(f"{hours}:0{minutes}")
elif 10<= minutes <= 59:
 print(f"{hours}:{minutes}")
