pythonset= set(("salman", "alfariz", "joseph","ashik")) 
print(pythonset)
print(type(pythonset))
dascset = {"salman","alfariz","joseph","ashik"}
print(dascset)
print(type(dascset))
pythonset.add("samiya")
dascset.remove("ashik")
print(dascset)
print(pythonset & dascset ,"are in both sets")
print(pythonset - dascset ,"are only in python")
print(pythonset|dascset ,"all student in both courec  ")
cource_dict={
    "Python": len(pythonset),
    "Data Science": len(dascset)
}
for cource,val in cource_dict.items():
    print(cource,":",val)
    
    
growth={key:value*2 for key,value in cource_dict.items()}
print(growth)


for course,value in growth.items():
    print(course,":",value)