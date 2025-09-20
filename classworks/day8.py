class Person:
    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age
        super().__init__(**kwargs)

    def show_detail(self):
        print(f"The person name is {self.name} and age is {self.age}")


class Employee(Person):
    def __init__(self, name, age, employee_id,**kwargs):
        super().__init__(name, age, **kwargs)
        self.employee_id = employee_id

    def show_detail(self):
        print(f"The employee name is {self.name}, age={self.age}, id={self.employee_id}")


class PartTime(Person):
    def __init__(self, name, age, working_hour, **kwargs):
        super().__init__(name, age, **kwargs)
        self.working_hour = working_hour

    def show_detail(self):
        print(f"The employee name is {self.name}, age={self.age}, Working_Hours={self.working_hour}")


class Consultant(Employee, PartTime):
    def __init__(self, name, age, employee_id, working_hour, project_name, **kwargs):
        super().__init__(name=name, age=age, employee_id=employee_id, working_hour=working_hour, **kwargs)
        self.project_name = project_name

    def show_detail(self):
        print(f"The employee name is {self.name} , age={self.age} , Employee_id={self.employee_id} , Working_Hours={self.working_hour} , Project_name={self.project_name}.")
# creating objects
stud1 = Person("Kevin", 26)
stud1.show_detail() 
stud1 = Employee("arun", 26,"t1d")
stud1.show_detail() 
stud1 = PartTime("akhil", 26,5.5)
stud1.show_detail() 
stud1 = Consultant("ravi", 26,"td1",5.5,"dcompany")
stud1.show_detail()