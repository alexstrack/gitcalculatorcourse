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


def menuoptions():
    """Display the menu options"""
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulo")
    print("7. Exit")


def display_history(history):
    """Display the history of calculations"""
    if not history:
        print("No calculations have been performed yet.")
        return
    print("\nCalculation History:")
    for entry in history:
        print(
            f"{entry['num1']} {entry['operation']} {entry['num2']} = {entry['result']}"
        )
    print()


def main():
    choice = 0
    history = []
    while choice != "7":
        menuoptions()
        choice = input("Enter choice (1-6): ")

        # Check if the choice is valid
        if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Invalid choice. It should be between 1 and 7.")
            return
        else:
            if choice == "7":
                print("Exiting the calculator. Goodbye!")
                display_history(history)
                break
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    result = add(num1, num2)
                    print(f"{num1} + {num2} = {result}")
                    history.append(
                        {
                            "num1": num1,
                            "num2": num2,
                            "operation": "add",
                            "result": result,
                        }
                    )
                elif choice == "2":
                    result = subtract(num1, num2)
                    print(f"{num1} - {num2} = {result}")
                    history.append(
                        {
                            "num1": num1,
                            "num2": num2,
                            "operation": "subtract",
                            "result": result,
                        }
                    )
                elif choice == "3":
                    result = multiply(num1, num2)
                    print(f"{num1} * {num2} = {result}")
                    history.append(
                        {
                            "num1": num1,
                            "num2": num2,
                            "operation": "multiply",
                            "result": result,
                        }
                    )
                elif choice == "4":
                    try:
                        result = divide(num1, num2)
                        print(f"{num1} / {num2} = {result}")
                        history.append(
                            {
                                "num1": num1,
                                "num2": num2,
                                "operation": "divide",
                                "result": result,
                            }
                        )
                    except ValueError as e:
                        print(f"Error: {e}")
                elif choice == "5":
                    result = power(num1, num2)
                    print(f"{num1} ** {num2} = {result}")
                    history.append(
                        {
                            "num1": num1,
                            "num2": num2,
                            "operation": "power",
                            "result": result,
                        }
                    )
                elif choice == "6":
                    try:
                        result = modulo(num1, num2)
                        print(f"{num1} % {num2} = {result}")
                        history.append(
                            {
                                "num1": num1,
                                "num2": num2,
                                "operation": "modulo",
                                "result": result,
                            }
                        )
                    except ValueError as e:
                        print(f"Error: {e}")


if __name__ == "__main__":
    main()
