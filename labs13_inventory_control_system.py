# Lab 13 - Inventory Control System

inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

while True:
    print("\n" + "=" * 40)
    print("       INVENTORY CONTROL SYSTEM")
    print("=" * 40)

    print("\nSelect an operation:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")

    try:
        choice = int(input("\nEnter your choice (1-5): "))

        if choice == 1:
            print("\n--- Current Inventory ---")
            for i, item in enumerate(inventory, start=1):
                print(f"{i}. {item}")

        elif choice == 2:
            item = input("Enter item name to add: ")

            if item.strip():
                inventory.append(item)
                print(f"[SUCCESS] '{item}' added to inventory.")
            else:
                print("[ERROR] Item name cannot be empty.")

        elif choice == 3:
            item = input("Enter item name to remove: ")

            if item in inventory:
                inventory.remove(item)
                print(f"[SUCCESS] '{item}' removed from inventory.")
            else:
                print(f"[ERROR] '{item}' not found in inventory.")

        elif choice == 4:
            inventory.sort()
            print("\n[SUCCESS] Inventory sorted alphabetically.")
            print("Updated Inventory:")

            for i, item in enumerate(inventory, start=1):
                print(f"{i}. {item}")

        elif choice == 5:
            print("\nThank you for using Inventory Control System!")
            print("Goodbye!")
            break

        else:
            print("[ERROR] Invalid choice! Please enter a number from 1 to 5.")

    except ValueError:
        print("[ERROR] Please enter a valid number.")
