from art import logo


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number.")


def calculator():
    print(logo)
    num1 = get_number("What is the first number?: ")

    while True:
        print("\nAvailable operations:")
        for symbol in OPERATIONS:
            print(symbol)

        operation = input("Pick an operation: ")

        if operation not in OPERATIONS:
            print("❌ Invalid operation.")
            continue

        num2 = get_number("What is the next number?: ")

        try:
            result = OPERATIONS[operation](num1, num2)
        except ValueError as e:
            print(f"❌ Error: {e}")
            continue

        print(f"✅ {num1} {operation} {num2} = {result}")

        choice = input(
            f"\nType 'y' to continue with {result}, "
            f"'n' to start new calculation, "
            f"or 'q' to quit: "
        ).lower()

        if choice == "y":
            num1 = result
        elif choice == "n":
            print("\n" * 2)
            calculator()
            return
        else:
            print("👋 Goodbye!")
            return


def main():
    calculator()


if __name__ == "__main__":
    main()
