# selecting a dictionary from a set of dictionaries ::
students = [
    {"id": 1, "name": "rajesh"},
    {"id": 2, "name": "rahul"},
    {"id": 3, "name": "sruthi"}
]
student_id = int(input("Enter student id: "))
present=[student for student in students if student.get("id")==student_id]
if present:
    print(f"the student is found at index:{students.index(present[0])+1}" )
    print(f"id = {present[0].get('id')} and name = {present[0].get('name')}")
else:
    print("student not found")