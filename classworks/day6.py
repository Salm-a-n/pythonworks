attendance=[18,20,19,15,21]
#in which day the attendance is ful......
for attend in attendance:
    if attend>=20:
        print(f"{attend} the attendance is full")
    else:
        print(f"{attend} attendance is not full")
# counting the number of full days .........
day=0
for element in attendance:
    if element>=20:
        day=day+1
print(f"The total number of full working days are {day}")
 #total attendance..............
total=0
for x in attendance:
    total+=x      
print(f"The total number of attendance in day are :{total}")
       
    