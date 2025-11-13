
history = []  # to store already done calculations


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b


def view_history():
    if not history:
        print("No history yet.")
    else:
        print("\n--- Calculation History ---")
        for item in history:
            print(item)
        print("---------------------------\n")


def clear_history():
    history.clear()
    print("History cleared!\n")


def calculator():
    while True:
        print("\nSimple Calculator")
        print("-----------------")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. View History")
        print("6. Clear History")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == '7':
            print("Goodbye!")
            break
        elif choice == '5':
            view_history()
            continue
        elif choice == '6':
            clear_history()
            continue

        # For math options (1–4), take two numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue

        if choice == '1':
            result = add(num1, num2)
            sign = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            sign = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            sign = "*"
        elif choice == '4':
            result = divide(num1, num2)
            sign = "/"
        else:
            print("Invalid option, try again!")
            continue

        print(f"Result: {result}")
        history.append(f"{num1} {sign} {num2} = {result}")


# Run the calculator
calculator()
