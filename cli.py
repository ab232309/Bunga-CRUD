import main

while True:
    print("\nStudent Database Operations:")
    print("1. Create Student")
    print("2. Read Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        year = float(input("Enter student year: "))
        main.create_student(name, age, year)
    elif choice == '2':
        main.read_students()
    elif choice == '3':
        student_id = int(input("Enter student ID to update: "))
        name = input("Enter updated name: ")
        age = int(input("Enter updated age: "))
        year = float(input("Enter updated year: "))
        main.update_student(student_id, name, age, year)
    elif choice == '4':
        student_id = int(input("Enter student ID to delete: "))
        main.delete_student(student_id)
    elif choice == '5':
        break
    else:
        print("Invalid choice.")
