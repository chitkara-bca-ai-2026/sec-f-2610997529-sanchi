def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def modulus(a, b):
    if b == 0:
        return None
    return a % b

def power(base, exp=2):
    return base ** exp

def format_number(n):
    if n == int(n):
        return int(n)
    return n

history = []

while True:
    print("\n===== ENTERPRISE MODULAR UTILITY CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power / Exponentiation")
    print("7. View Calculation History")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("Invalid choice!")
        continue

    if choice == "8":
        print("Thank you for using the calculator!")
        break

    if choice == "7":
        if history:
            print("\nCalculation History")
            for item in history:
                print(item)
        else:
            print("No calculations performed yet.")
        continue

    try:
        a = float(input("Enter first number: "))
        b = None

        if choice == "6":
            exp = input("Enter exponent (press Enter for default 2): ")
            if exp == "":
                result = power(a)
                expression = f"{a} ** 2"
            else:
                b = float(exp)
                result = power(a, b)
                expression = f"{a} ** {b}"

        else:
            b = float(input("Enter second number: "))

            if choice == "1":
                result = add(a, b)
                expression = f"{a} + {b}"

            elif choice == "2":
                result = subtract(a, b)
                expression = f"{a} - {b}"

            elif choice == "3":
                result = multiply(a, b)
                expression = f"{a} * {b}"

            elif choice == "4":
                result = divide(a, b)
                expression = f"{a} / {b}"

            elif choice == "5":
                result = modulus(a, b)
                expression = f"{a} % {b}"

        if result is None:
            print("Error: Cannot divide or find modulus by zero.")
        else:
            result = format_number(result)
            print("RESULT:", result)
            history.append(f"{expression} = {result}")

    except ValueError:
        print("Invalid input! Please enter numbers.")