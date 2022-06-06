student_name = input()
grade = 1
sum_grades = 0
times_failed = 0
while grade <= 12:
    yearly_grading = float(input())
    sum_grades += yearly_grading
    if yearly_grading < 4:
        sum_grades -= yearly_grading
        times_failed += 1
    else:
        grade += 1
    if times_failed == 2:
        break
if times_failed == 0 or times_failed == 1:
    grade -= 1
average_grade = sum_grades / grade
if times_failed == 2:
    print(f"{student_name} has been excluded at {grade} grade")
elif times_failed == 1:
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
else:
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
