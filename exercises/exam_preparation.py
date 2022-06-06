bad_grades_acceptable = int(input())
problem_name = ""
sum_score = 0
bad_grades = 0
problems_solved = 0
last_problem = ""
while problem_name != "Enough":
    problem_name = input()
    if problem_name == "Enough":
        break
    grade = int(input())
    sum_score += grade
    problems_solved += 1
    last_problem = problem_name
    if grade <= 4:
        bad_grades += 1
    if bad_grades == bad_grades_acceptable:
        break
if bad_grades == bad_grades_acceptable:
    print(f"You need a break, {bad_grades} poor grades.")
else:
    print(f"Average score: {(sum_score / problems_solved):.2f}")
    print(f"Number of problems: {problems_solved}")
    print(f"Last problem: {last_problem}")
