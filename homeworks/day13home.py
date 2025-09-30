import os
filename = "students.txt"
if os.path.exists(filename):
    print("Successfully fetched the file. Here are the student names in 'students.txt':")
    with open(filename, "r") as file:
        content = file.read()
        print(content)
else:
    print("Oops, No such file exists. A new file will be created to store names.")
no_of_name=int(input("enter the No:of students you want to add:"))
with open(filename,"a") as newfile:
    for n in range(1,no_of_name+1):
        name=input(f"Enter the name of student-{n} : ")
        newfile.write(name +"\n")
print("The new file contain the following names : ")
with open(filename,"r") as last_file:
    student_names=last_file.read()
    print(student_names)

 