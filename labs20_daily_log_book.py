import os

def append_entry(filename, entry):
    with open(filename, "a") as file:
        file.write(entry + "\n")
    print(f"New entry logged to '{filename}'.")

def display_log(filename):
    with open(filename, "r") as file:
        entries = file.readlines()

    print("\n========== DAILY LOG BOOK ==========")

    if entries:
        for i, entry in enumerate(entries, 1):
            print(f"[{i:02d}] {entry.strip()}")

        print("\nTotal Logged Entries:", len(entries))
    else:
        print("No log entries found.")

filename = "daily_log.txt"

if not os.path.exists(filename):
    with open(filename, "w") as file:
        file.write("09:00 AM - System server startup verified.\n")
        file.write("10:30 AM - Morning attendance synchronized.\n")
        file.write("02:15 PM - Network security patch applied.\n")

while True:
    print("\n===== OFFICE DAILY LOG BOOK =====")
    print("1. Add Log Entry")
    print("2. Display Complete Log")
    print("3. Exit")

    choice = input("Enter choice (1-3): ")

    if choice == "1":
        entry = input("Enter log entry: ")

        if entry.strip():
            append_entry(filename, entry)
        else:
            print("Log entry cannot be empty.")

    elif choice == "2":
        display_log(filename)

    elif choice == "3":
        print("Thank you for using Daily Log Book. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1-3.")