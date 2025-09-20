class Employee:
    def __init__(self, name, role, **kwargs):
        self.name = name
        self.role = role
        super().__init__(**kwargs)

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}")

class Trainee(Employee):
    def __init__(self, name, role, specialization, **kwargs):
        super().__init__(name=name, role=role, **kwargs)
        self.specialization = specialization

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}, Specialization: {self.specialization}")

class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style, **kwargs):
        super().__init__(name=name, role=role, **kwargs)
        self.yoga_style = yoga_style

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}, Yoga Style: {self.yoga_style}")

class MultiTrainer(Trainee, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style, **kwargs):
        super().__init__(name=name, role=role, specialization=specialization, yoga_style=yoga_style, **kwargs)

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}, Specialization: {self.specialization}, Yoga Style: {self.yoga_style}")

# Creating objects and calling the method in each class
employee = Employee("Alfariz", "Manager")
employee.display()
trainer = Trainee("Salman", "Trainer", "Strength Training")
trainer.display()
yoga_instructor = YogaInstructor("Ashik", "Yoga Instructor", "Kukkudasanam")
yoga_instructor.display()
multi_trainer = MultiTrainer("Joseph", "Yoga Instructor", "Shavasanam", "Yoga_style")
multi_trainer.display()