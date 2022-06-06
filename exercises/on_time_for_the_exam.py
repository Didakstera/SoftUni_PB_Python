exam_hour = int(input())
exam_minutes = int(input())
student_hour = int(input())
student_minutes = int(input())
hours_early = 0
hours_late = 0
minutes_early = 0
minutes_late = 0
on_time = 'no'
if exam_hour == student_hour:
    if exam_minutes > student_minutes:
      minutes_early = exam_minutes - student_minutes
    elif exam_minutes < student_minutes:
      minutes_late = student_minutes - exam_minutes
    elif exam_minutes == student_minutes:
        on_time = "yes"
elif exam_hour < student_hour:
    if exam_minutes > student_minutes:
        minutes_late = 60 - exam_minutes + student_minutes
        hours_late = student_hour - exam_hour - 1
    elif exam_minutes <= student_minutes:
        minutes_late = student_minutes - exam_minutes
        hours_late = student_hour - exam_hour
elif exam_hour > student_hour:
    if exam_minutes >= student_minutes:
        minutes_early = exam_minutes - student_minutes
        hours_early = exam_hour - student_hour
    if exam_minutes < student_minutes:
        minutes_early = 60 - student_minutes + exam_minutes
        hours_early = exam_hour - student_hour - 1
if on_time == "yes":
    print("On time")
elif on_time == "no":
    if exam_hour == student_hour and exam_minutes > student_minutes:
        if exam_minutes - student_minutes <= 30:
          print("On time")
          print(f"{minutes_early} minutes before the start")
        elif exam_minutes - student_minutes > 30:
          print("Early")
          print(f"{minutes_early} minutes before the start")
    elif exam_hour == student_hour and exam_minutes < student_minutes:
        print("Late")
        print(f"{minutes_late} minutes after the start")
    elif exam_hour < student_hour:
        if hours_late < 1:
            print("Late")
            print(f"{minutes_late} minutes after the start")
        elif hours_late >= 1 and minutes_late <=9:
            print("Late")
            print(f"{hours_late}:0{minutes_late} hours after the start")
        elif hours_late >= 1 and minutes_late > 9:
            print("Late")
            print(f"{hours_late}:{minutes_late} hours after the start")
    elif exam_hour > student_hour:
        if hours_early < 1:
            if minutes_early <= 30:
                print("On time")
                print(f"{minutes_early} minutes before the start")
            if minutes_early > 30:
                print("Early")
                print(f"{minutes_early} minutes before the start")
        if hours_early >= 1 and minutes_early <= 9:
            print("Early")
            print(f"{hours_early}:0{minutes_early} hours before the start")
        if hours_early >= 1 and minutes_early > 9:
            print("Early")
            print(f"{hours_early}:{minutes_early} hours before the start")
