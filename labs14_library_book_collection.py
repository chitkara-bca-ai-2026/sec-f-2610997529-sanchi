
books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2021", "AI"),
    ("Clean Code", "Robert C. Martin", "2008", "Software Engineering")
]

library_categories = set()

for title, author, year, category in books:
    library_categories.add(category)

student_wishlist = {
    "AI",
    "Cloud Computing",
    "Robotics",
    "Cybersecurity"
}


while True:

    print("\n==========================================")
    print("       LIBRARY BOOK & CATEGORY MANAGER")
    print("==========================================")

    print("\nSelect an operation:")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("[ERROR] Invalid choice! Please enter 1-6.")
        continue

  
    if choice == "1":

        print("\n--- Current Library Catalog (Fixed Records) ---")

        for i, (title, author, year, category) in enumerate(books, 1):
            print(f'{i}. "{title}" by {author} ({year}) | Genre: {category}')

        print("Total Books:", len(books))

    
    elif choice == "2":

        print("\n--- Add New Book Record ---")

        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = input("Enter publication year: ")
        category = input("Enter category/genre: ")

        if title and author and year and category:
            new_book = (title, author, year, category)

            books.append(new_book)
            library_categories.add(category)

            print(f'\n[SUCCESS] "{title}" added as an immutable catalog record.')
            print(f'[INFO] Category set updated with: "{category}"')

        else:
            print("[ERROR] All fields are required.")

    
    elif choice == "3":

        print("\n--- Unique Categories Available in Library (Set) ---")

        for category in sorted(library_categories):
            print("-", category)

        print("Total Unique Genres:", len(library_categories))

    
    elif choice == "4":

        print("\n--- Add to Student Wishlist ---")

        requested_category = input("Enter requested category: ")

        if requested_category:
            student_wishlist.add(requested_category)
            print(f'[SUCCESS] "{requested_category}" added to student wishlist.')

        else:
            print("[ERROR] Category cannot be empty.")

    
    elif choice == "5":

        print("\n============== CATEGORY GAP ANALYSIS ==============")

        print("Library Holdings (Set):", sorted(library_categories))
        print("Student Wishlist (Set):", sorted(student_wishlist))

        
        intersection = library_categories & student_wishlist

        
        difference = student_wishlist - library_categories

        
        union = library_categories | student_wishlist

        print("\n1. Already in Stock (Intersection &):")
        print(sorted(intersection))

        print("\n2. Purchase Order Needed (Difference -):")
        print(sorted(difference))

        print("\n3. Full Combined Genre Coverage (Union |):")
        print(sorted(union))

    # Choice 6: Exit
    elif choice == "6":

        print("\nThank you for using the Library Manager. Goodbye!")
        break
