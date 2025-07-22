# Calculator
class Calculator:
    def __init__(self):
        self.num1=0
        self.num2=0
        self.ar=" "
    def input_var(self):
        self.num1 = float(input("Enter first number: "))
        self.num2 = float(input("Enter second number: "))
        self.ar = input("Enter Arithmetic operation: ")
    def calculate(self):
        if self.ar == "+":
            sum= self.num1 + self.num2
            print(f"Sum is: {sum}")
        elif self.ar == "-":
            diff = self.num1 - self.num2
            print(f"Difference is: {diff}")
        elif self.ar == "*":
            pro = self.num1*self.num2
            print(f"Product is: {pro}")
        elif self.ar == "/":
            div = self.num1/self.num2
            print(f"Division is: {div}")
        else :
            print("Invalid input")

obj = Calculator()
obj.input_var()
obj.calculate()
