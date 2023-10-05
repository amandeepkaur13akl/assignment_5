class Calculator:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        return self.num2 // self.num1
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
obj = Calculator(num1,num2)
Add = obj.add()
Sub = obj.subtract()
Mul = obj.multiply()
Div = obj.divide()
print(f"Add:{Add} \nSubtract:{Sub} \nMultiply:{Mul} \nDivide:{Div} ")