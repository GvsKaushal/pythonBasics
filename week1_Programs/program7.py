class Calculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            return None

def get_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    calculator = Calculator()

    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '5':
            break

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        if choice == '1':
            result = calculator.add(num1, num2)
        elif choice == '2':
            result = calculator.subtract(num1, num2)
        elif choice == '3':
            result = calculator.multiply(num1, num2)
        elif choice == '4':
            result = calculator.divide(num1, num2)
        else:
            print("Invalid choice. Please try again.")

        if result is not None:
            print("Result:", result)

if __name__ == "__main__":
    main()