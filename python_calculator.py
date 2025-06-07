# calculator.py
"""
A simple calculator application for learning Git
"""


def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract two numbers"""
    return a - b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """Raise a to the power of b"""
    return a**b


def modulo(a, b):
    """Return the remainder of a divided by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b


def main():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulo")

    choice = input("Enter choice (1-6): ")

    if choice in ["1", "2", "3", "4", "5", "6"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == "2":
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == "3":
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == "4":
            try:
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "5":
            result = power(num1, num2)
            print(f"{num1} ** {num2} = {result}")
        elif choice == "6":
            try:
                result = modulo(num1, num2)
                print(f"{num1} % {num2} = {result}")
            except ValueError as e:
                print(f"Error: {e}")

    else:
        print("Invalid choice. Please select a valid option (1-6).")


if __name__ == "__main__":
    main()
