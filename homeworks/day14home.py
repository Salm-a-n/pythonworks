# LuckyDraw_system...
import random
import math
Customer_name = input("enter the Customer names separated by comma: ")
names = [n.strip() for n in Customer_name.split(",")]
new_names = list(set(names))
random.shuffle(new_names)
winners = random.sample(new_names, k=2)
reversed_name = [name[::-1] for name in winners]
print("the reversed name of winners is", reversed_name)
print("the winners are:")
for x in winners:
    print(x)
total_number = len(new_names)
print("the total number of participants is", total_number)
root = math.sqrt(total_number)
print("the square root of total number of participants is", root)
rounded_value = round(root)
print("the rounded value is", rounded_value)