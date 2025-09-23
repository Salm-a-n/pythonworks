from abc import ABC,abstractmethod
class user(ABC):
    def __init__(self,name,year):
        self.name=name
        self.year=year
    def years(self):
        current_year=2025
        return current_year-self.year
    @abstractmethod
    def specific_role(self):
        pass
    def __str__(self):
        return f"\n  Name: {self.name} ,   Role: {self.specific_role()} ,   Years on platform: {self.years()} \n "
class Customer(user):
    def specific_role(self):
        return "Customer"

class Vendor(user):
    def specific_role(self):
        return "Vendor"

salman = Customer("Salman", 2004)
allu = Vendor("Allu", 2008)

print(salman)

print(allu)
