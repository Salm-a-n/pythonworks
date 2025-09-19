class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_detail(self):
        print(f"The person name is {self.name} and age is {self.age}")


class Employee(Person):
    def __init__(self, name, age, employee_id):
        Person.__init__(self, name, age)
        self.employee_id = employee_id

    def show_detail(self):
        print(f"The employee name is {self.name}, age={self.age}, id={self.employee_id}")


class PartTime(Person):
    def __init__(self, name, age, working_hour):
        Person.__init__(self, name, age)
        self.working_hour = working_hour

    def show_detail(self):
        print(f"The employee name is {self.name}, age={self.age}, Working_Hours={self.working_hour}")


class Consultant(Employee, PartTime):
    def __init__(self, name, age, employee_id, working_hour, project_name):
        Employee.__init__(self, name, age, employee_id)
        PartTime.__init__(self, name, age, working_hour)
        self.project_name = project_name

    def show_detail(self):
        print(f"The employee name is {self.name} , age={self.age} , Employee_id={self.employee_id} , Working_Hours={self.working_hour} , Project_name={self.project_name}.")
stud1 = Person("Kevin", 26)
stud1.show_detail() 
stud1 = Employee("Kevin", 26,"t1d")
stud1.show_detail() 
stud1 = PartTime("Kevin", 26,5.5)
stud1.show_detail() 
stud1 = Consultant("Kevin", 26,"td1",5.5,"dcompany")
stud1.show_detail()   