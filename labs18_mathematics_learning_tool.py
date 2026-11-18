def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

while True:
    print("\n===== MATHEMATICS LEARNING TOOL =====")
    print("1. Calculate Factorial")
    print("2. Generate Fibonacci Series")
    print("3. Exit")

    choice = input("Enter choice (1-3): ")

    if choice == "1":
        try:
            n = int(input("Enter a non-negative integer: "))

            if n < 0:
                print("Please enter a non-negative number.")
            else:
                print("Factorial of", n, "is:", factorial(n))

        except ValueError:
            print("Invalid input! Enter an integer.")

    elif choice == "2":
        try:
            terms = int(input("Enter number of terms to generate: "))

            if terms < 0:
                print("Please enter a non-negative number.")
            else:
                series = []
                for i in range(terms):
                    series.append(fibonacci(i))

                print("Fibonacci Series:", series)

        except ValueError:
            print("Invalid input! Enter an integer.")

    elif choice == "3":
        print("Thank you for using the Mathematics Learning Tool. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1-3.")