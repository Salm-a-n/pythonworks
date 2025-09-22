class Account:
    def __init__(self, holder_name, balance):
        self._holder_name = holder_name
        self._balance = balance

    def __add__(self, other):
        return self._balance + other._balance

    def details(self):
        return f"Account holder name: {self._holder_name}, Available balance: ₹{self._balance:.2f}"

class SavingsAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.05

class CurrentAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.02

# Create account objects
Ravi = SavingsAccount("Ravi", 10000.0)
Anjali = CurrentAccount("Anjali", 15000.0)

# Displaying details 
print("Savings Account:")
print(Ravi.details())
print(f"Interest (5%): ₹{Ravi.calculate_interest():.2f}")

print("Current Account:")
print(Anjali.details())
print(f"Interest (2%): ₹{Anjali.calculate_interest():.2f}")

total_balance = Ravi + Anjali
print("Total Combined Balance:")
print(f"₹{total_balance:.2f}")