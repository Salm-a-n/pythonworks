import os

user_input = input("Enter the name of a new item: ")
if not os.path.exists("items.txt"):
    with open("items.txt", "w") as file:
        file.write(user_input + "\n")
else:
    with open("items.txt", "a") as file:
        file.write(user_input + "\n")

print("\nCurrent list of items:")
with open("items.txt", "r") as file:
    for line in file:
        print(line)