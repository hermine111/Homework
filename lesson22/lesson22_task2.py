# 2. Class Exercise:
# Create a Python class representing a basic calculator with methods for addition,
# subtraction, multiplication, and division.


class BasicCalculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2


calculator = BasicCalculator()
print(calculator.add(589, 1239))
print(calculator.subtract(90, 74))
print(calculator.multiply(89, 878))
print(calculator.divide(85015, 155))