import random
import math
name = input("enter the names separated by comma: ")
names = [n.strip() for n in name.split(",")]
new_names = list(set(names))
selected_name = random.choice(new_names)
reversed_name = selected_name[::-1]
print("the reversed name is", reversed_name)
total_number = len(new_names)
print("the total number of guest is", total_number)
root = math.sqrt(total_number)
print("the square root of total number of guest is", root)
rounded_value = round(root)
print("the rounded value is", rounded_value)
