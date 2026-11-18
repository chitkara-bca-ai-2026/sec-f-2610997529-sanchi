students = {
    "101": {
        "Name": "Aman",
        "Branch": "BCA AI",
        "Semester": "2",
        "Marks": [85, 90, 78]
    },
    "102": {
        "Name": "Riya",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [92, 88, 95]
    },
    "103": {
        "Name": "Karan",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [74, 80, 82]
    }
}

while True:

    print("\n====================================")
    print("STUDENT INFORMATION MANAGEMENT SYSTEM")
    print("====================================")

    print("\nSelect an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid choice! Please enter 1-7.")
        continue

    if choice == "1":

        print("\n--- Enrolled Student Records ---")

        for roll, student in students.items():
            print(f"\nRoll No: {roll}")
            print("Name:", student["Name"])
            print("Branch:", student["Branch"])
            print("Semester:", student["Semester"])
            print("Marks:", student["Marks"])

        print("\nTotal Enrolled Students:", len(students))

    elif choice == "2":

        roll = input("Enter Roll Number to search: ")

        student = students.get(roll)

        if student:
            print("\n[FOUND] Record for Roll No:", roll)
            print("Name:", student["Name"])
            print("Branch:", student["Branch"])
            print("Semester:", student["Semester"])
            print("Marks:", student["Marks"])
        else:
            print("Record not found.")

    elif choice == "3":

        print("\n--- Register New Student ---")

        roll = input("Enter Roll Number: ")

        if roll in students:
            print("Roll Number already exists.")
            continue

        name = input("Enter Student Name: ")
        branch = input("Enter Branch: ")
        semester = input("Enter Semester: ")

        try:
            marks = []

            for i in range(3):
                mark = int(input(f"Enter marks in Subject {i+1}: "))
                if mark < 0 or mark > 100:
                    raise ValueError
                marks.append(mark)

            students[roll] = {
                "Name": name,
                "Branch": branch,
                "Semester": semester,
                "Marks": marks
            }

            print(f"\n[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully.")

        except ValueError:
            print("Invalid marks! Enter marks between 0 and 100.")

    elif choice == "4":

        roll = input("Enter Roll Number to update: ")

        if roll in students:

            print("Current Details:", students[roll])
            print("1. Branch")
            print("2. Semester")

            field = input("Choose field to update (1 or 2): ")

            if field == "1":
                new_value = input("Enter new branch: ")
                students[roll]["Branch"] = new_value
                print("[SUCCESS] Branch updated successfully.")

            elif field == "2":
                new_value = input("Enter new semester: ")
                students[roll]["Semester"] = new_value
                print("[SUCCESS] Semester updated successfully.")

            else:
                print("Invalid field choice.")

        else:
            print("Student record not found.")

    elif choice == "5":

        roll = input("Enter Roll Number for Academic Performance: ")

        if roll in students:

            student = students[roll]
            total = sum(student["Marks"])
            average = total / len(student["Marks"])

            result = "PASS" if average >= 40 else "FAIL"

            print("\n========== ACADEMIC REPORT ==========")
            print("Student Name:", student["Name"])
            print("Roll Number:", roll)
            print("Subject Marks:", student["Marks"])
            print("Total Marks:", total, "/ 300")
            print("Average Marks:", round(average, 2), "%")
            print("Final Result:", result)
            print("=====================================")

        else:
            print("Student record not found.")

    elif choice == "6":

        roll = input("Enter Roll Number to delete: ")

        deleted = students.pop(roll, None)

        if deleted:
            print(f"[SUCCESS] Record for '{deleted['Name']}' (Roll No: {roll}) deleted successfully.")
        else:
            print("Student record not found.")

    elif choice == "7":

        print("\nThank you for using Student Information System.")
        print("Goodbye!")
        break