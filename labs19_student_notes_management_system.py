import os

def write_notes(filename, content):
    with open(filename, "w") as file:
        file.write(content)
    print("Notes successfully saved.")

def read_notes(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return file.read()
    else:
        return "No notes file exists yet."

while True:
    print("\n===== STUDENT NOTES MANAGEMENT SYSTEM =====")
    print("1. Write / Save Notes")
    print("2. View Saved Notes")
    print("3. Exit")

    choice = input("Enter choice (1-3): ")

    if choice == "1":
        notes = input("Enter notes to save: ")
        write_notes("notes.txt", notes)

    elif choice == "2":
        content = read_notes("notes.txt")
        print("\n--- Notes Content (notes.txt) ---")
        print(content)

    elif choice == "3":
        print("Thank you for using the Notes Management System. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1-3.")