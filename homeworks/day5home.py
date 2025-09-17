Frontend={"salman","vishnu","alfariz","ashik","joseph"}
Backend={"salman","vishnu","alfariz","ashik","joseph","samiya","nithin"}
# adding a new student to the backend set 
Backend.add("saurav")
#removing  one value from set .
Frontend.discard("joseph")#pop will terminate different values on each execution
# print(Frontend)
# for printing common names in both set .
both=Backend&Frontend
print(f"The student in both list is {both}")
# The student only in backend .
Onlbac=Backend-Frontend
print(f" The student only in backend are {Onlbac}")
# no:of unique names .
uniq=Backend^Frontend
print(f"The count of  unique name in both sets are {len(uniq)}")

FBdict={"frontend":len(Frontend),
        "backend":len(Backend)
        }
#printing each key and value using for loop
print("the number of student in each unit are ")
for k,v in FBdict.items():
    print(k,":",v)
#fullstack! students number 
fullstack={"fullstack":sum(x for x in FBdict.values())}
print(fullstack)
# print(type(fullstack))