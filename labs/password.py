username = input()
password = input()
true_password = ""
while true_password != password:
    true_password = input()
print(f"Welcome {username}!")
