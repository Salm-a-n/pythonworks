# performing multiplication table of a number upto 10::
num=int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i} ")