import sqlite3

# Connect to an SQLite database (or create it if it doesn't exist)
db = sqlite3.connect('student_database.sqlite')
cursor = db.cursor()

# Create the 'students' table if it doesn't exist
def create_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        signup_date TEXT,
        lessons INTEGER   
    )
    ''')
    db.commit()

# Call the create_table function to ensure the table is created
create_table()

# Create a new student record
def create_student(name, age, signup_date, lessons):
    sql = "INSERT INTO students (name, age, year, signup_date, lessons) VALUES (?, ?, ?, ?, ?)"
    values = (name, age, signup_date, lessons)
    cursor.execute(sql, values)
    db.commit()


# Read all student records
def read_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return students  # Return the list of students


# Update a student record
def update_student(student_id, name, age, signup_date, lessons):
    sql = "UPDATE students SET name = ?, age = ?, signup_date = ? WHERE id = ? lessons = ?"
    values = (name, age, signup_date, lessons, student_id)
    cursor.execute(sql, values)
    db.commit()


# Delete a student record
def delete_student(student_id):
    sql = "DELETE FROM students WHERE id = ?"
    values = (student_id,)
    cursor.execute(sql, values)
    db.commit()

if __name__ == "__main__":
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
            create_student(name, age, year)
        elif choice == '2':
            read_students()
        elif choice == '3':
            student_id = int(input("Enter student ID to update: "))
            name = input("Enter updated name: ")
            age = int(input("Enter updated age: "))
            year = float(input("Enter updated year: "))
            update_student(student_id, name, age, year)
        elif choice == '4':
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

    # Close the database connection
    db.close()
