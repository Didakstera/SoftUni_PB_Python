import sys
min_number = sys.maxsize
command = ""
while command != "Stop":
    command = input()
    if command == "Stop":
        break
    number = int(command)
    if number < min_number:
        min_number = number
print(min_number)
