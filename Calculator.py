import math
from datetime import datetime


class AdvancedCalculator:
    def __init__(self):
        self.history = []

    def log(self, operation, result):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append(f"{timestamp} | {operation} = {result}")

    def add(self, a, b):
        result = a + b
        self.log(f"{a} + {b}", result)
        return result

    def subtract(self, a, b):
        result = a - b
        self.log(f"{a} - {b}", result)
        return result

    def multiply(self, a, b):
        result = a * b
        self.log(f"{a} * {b}", result)
        return result

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        result = a / b
        self.log(f"{a} / {b}", result)
        return result

    def power(self, a, b):
        result = a ** b
        self.log(f"{a} ^ {b}", result)
        return result

    def sqrt(self, a):
        if a < 0:
            return "Error: Negative input"
        result = math.sqrt(a)
        self.log(f"sqrt({a})", result)
        return result

    def factorial(self, a):
        if a < 0 or not a.is_integer():
            return "Error: Invalid input"
        result = math.factorial(int(a))
        self.log(f"{int(a)}!", result)
        return result

    def show_history(self):
        if not self.history:
            return "No calculations yet."
        return "\n".join(self.history)


def menu():
    print("\n=== Advanced Python Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Factorial")
    print("8. Show History")
    print("9. Exit")


calc = AdvancedCalculator()

while True:
    menu()
    choice = input("Choose an option (1-9): ")

    try:
        if choice == '1':
            a, b = map(float, input("Enter two numbers: ").split())
            print("Result:", calc.add(a, b))

        elif choice == '2':
            a, b = map(float, input("Enter two numbers: ").split())
            print("Result:", calc.subtract(a, b))

        elif choice == '3':
            a, b = map(float, input("Enter two numbers: ").split())
            print("Result:", calc.multiply(a, b))

        elif choice == '4':
            a, b = map(float, input("Enter two numbers: ").split())
            print("Result:", calc.divide(a, b))

        elif choice == '5':
            a, b = map(float, input("Enter base and exponent: ").split())
            print("Result:", calc.power(a, b))

        elif choice == '6':
            a = float(input("Enter number: "))
            print("Result:", calc.sqrt(a))

        elif choice == '7':
            a = float(input("Enter number: "))
            print("Result:", calc.factorial(a))

        elif choice == '8':
            print("\n--- Calculation History ---")
            print(calc.show_history())

        elif choice == '9':
            print("Calculator closed.")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid input. Please enter numbers correctly.")
