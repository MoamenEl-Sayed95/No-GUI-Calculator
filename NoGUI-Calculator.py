class Calculator:
    def __init__(self):
        print("Calculator Initialized!")

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        return a / b

    def exponentiate(self, a, b):
        return a**b


def main():
    calc = Calculator()

    while True:
        print("\nSimple Calculator (OOP-Based)")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice in ["1", "2", "3", "4", "5"]:
            try:
                num1 = float(input("Enter a first number: "))
                num2 = float(input("Enter a second number: "))

                if choice == "1":
                    result = f"{num1} + {num2} = {calc.add(num1, num2)}"
                elif choice == "2":
                    result = f"{num1} + {num2} = {calc.subtract(num1, num2)}"

                elif choice == "3":
                    result = f"{num1} + {num2} = {calc.multiply(num1, num2)}"

                elif choice == "4":
                    result = f"{num1} + {num2} = {calc.divide(num1, num2)}"

                elif choice == "5":
                    result = f"{num1} + {num2} = {calc.exponentiate(num1, num2)}"

                print(f"Result: {result}")
            except ValueError:
                print("Invalid input! Please enter valid numbers.")

        elif choice == "6":
            print("Exiting Calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-6.")


if __name__ == "__main__":
    main()

# Created By Programmer Moamen Abouhaty