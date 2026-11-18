def calculate_results(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

def display_student(roll, student):
    total, average = calculate_results(student["Marks"])
    print(f"Roll No: {roll} | Name: {student['Name']} | Marks: {student['Marks']} | Total: {total} | Average: {average:.2f}")

def add_student(records, roll, name, marks):
    if roll in records:
        print("Roll Number already exists.")
    else:
        records[roll] = {
            "Name": name,
            "Marks": marks
        }
        print("Student added successfully.")

students = {
    "101": {"Name": "Aman", "Marks": [85, 90, 78]},
    "102": {"Name": "Riya", "Marks": [92, 88, 95]},
    "103": {"Name": "Karan", "Marks": [74, 80, 82]}
}

while True:
    print("\n===== STUDENT RECORDS MANAGEMENT SYSTEM =====")
    print("1. Display All Students")
    print("2. Add New Student")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        print("\n--- All Student Records ---")
        for roll, student in students.items():
            display_student(roll, student)
        print("Total Students:", len(students))

    elif choice == "2":
        roll = input("Enter Roll Number: ")

        if roll in students:
            print("Roll Number already exists.")
            continue

        name = input("Enter Student Name: ")

        try:
            marks = []
            for i in range(3):
                mark = int(input(f"Enter marks for Subject {i+1}: "))
                if mark < 0 or mark > 100:
                    raise ValueError
                marks.append(mark)

            add_student(students, roll, name, marks)

        except ValueError:
            print("Enter valid marks between 0 and 100.")

    elif choice == "3":
        roll = input("Enter Roll Number to search: ")

        if roll in students:
            display_student(roll, students[roll])
        else:
            print("Record not found for Roll No:", roll)

    elif choice == "4":
        print("Thank you for using Student Records System. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1-4.")