# craeting a calclulator using classes and objects ::
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    # def divide(self):
    #         return self.num1 / self.num2
    def divide(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return "Cannot divide a number by zero"
        
num1 = float(input("Enter first number: "))
operator = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))      
calc = Calculator(num1, num2)
if operator == "+":
    print(f"Result: {calc.add()}")
elif operator == "-":
    print(f"Result: {calc.subtract()}")
elif operator == "*":
    print(f"Result: {calc.multiply()}")
elif operator == "/":
    print(f"Result: {calc.divide()}")
else:
    print("Invalid operation")