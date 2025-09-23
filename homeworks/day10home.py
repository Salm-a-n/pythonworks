from abc import ABC,abstractmethod
class User(ABC):
    def __init__(self,name,account_year):
        self.name=name
        self.account_year=account_year
    def account_age(self):
        current_year=2025
        return current_year - self.account_year
    @abstractmethod
    def get_role(self):
        pass
    @abstractmethod
    def __str__(self):
       pass
class Admin(User):
    def get_role(self):
        return "Admin"
    def __str__(self):
        return f"The Role of {self.name} is {self.get_role()} and Account was created in {self.account_year} And Account Age is {self.account_age()}"
class Guest(User):
    def get_role(self):
        return "Guest"
    def __str__(self):
        return f"The Role of {self.name} is {self.get_role()} and Account was created in {self.account_year} And Account Age is {self.account_age()}"
   
Admin_name=Admin("salman",2008)
Guest_name=Guest("abid",2010)
print(Admin_name)
print(Guest_name)