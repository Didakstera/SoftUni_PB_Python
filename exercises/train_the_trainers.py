people_asses = int(input())
input_line = input()
all_grades_sum = 0
grades_count = 0
while input_line != "Finish":
    presentation = input_line

    summary = 0
    for i in range(1, people_asses + 1):
        current_grade = float(input())
        grades_count += 1
        all_grades_sum = all_grades_sum + current_grade
        summary = summary + current_grade

    avg_grade_current = summary / people_asses
    print(f"{presentation} - {avg_grade_current:.2f}.")

    input_line = input()

total_avg_grade = all_grades_sum / grades_count
print(f"Student's final assessment is {total_avg_grade:.2f}.")
