architect_name = input()
total_projects = int(input())
hours_for_a_project = 3
hours_total = hours_for_a_project * total_projects
print(f"The architect {architect_name} will need {hours_total}", end=" ")
print(f"hours to complete {total_projects} project/s.")