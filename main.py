import sqlite3
import datetime

# Connect to an SQLite database (or create it if it doesn't exist)
db = sqlite3.connect('student_database.sqlite')
cursor = db.cursor()

def calculate_baptism_date(signup_date, lessons_listened):
    # Convert the signup_date to a datetime object
    signup_date_obj = datetime.datetime.strptime(signup_date, "%Y-%m-%d")

    # Add 6 months to the signup_date
    estimated_baptism_date = signup_date_obj + datetime.timedelta(days=180)

    # Add additional days based on the number of lessons listened (maximum 28 lessons)
    additional_days = min(lessons_listened, 28)
    estimated_baptism_date += datetime.timedelta(days=additional_days)

    return estimated_baptism_date.strftime("%Y-%m-%d")


# Create the 'students' table if it doesn't exist
def create_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        signup_date TEXT,
        lessons INTEGER,
        estbaptism_date TEXT
    )
    ''')
    db.commit()

# Call the create_table function to ensure the table is created
create_table()

# Create a new student record
def create_student(name, age, signup_date, lessons):
    try:
        sql = "INSERT INTO students (name, age, signup_date, lessons, estbaptism_date) VALUES (?, ?, ?, ?, NULL)"
        values = (name, age, signup_date, lessons)
        cursor.execute(sql, values)

        # Calculate the estimated baptism date
        baptism_date = calculate_baptism_date(signup_date, lessons)

        # Update the record with the calculated baptism date
        update_baptism_date_sql = "UPDATE students SET estbaptism_date = ? WHERE id = ?"
        update_baptism_date_values = (baptism_date, cursor.lastrowid)
        cursor.execute(update_baptism_date_sql, update_baptism_date_values)

        db.commit()
    except Exception as e:
        print(f"Error in create_student: {e}")



# Read all student records
def read_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return students  # Return the list of students


# Update a student record
def update_student(student_id, name, age, signup_date, lessons):
    try:
        # Update student information
        update_sql = "UPDATE students SET name = ?, age = ?, signup_date = ?, lessons_listened = ? WHERE id = ?"
        update_values = (name, age, signup_date, lessons, student_id)
        cursor.execute(update_sql, update_values)

        # Update estimated baptism date
        baptism_date = calculate_baptism_date(signup_date, lessons)
        update_baptism_date_sql = "UPDATE students SET estimated_baptism_date = ? WHERE id = ?"
        update_baptism_date_values = (baptism_date, student_id)
        cursor.execute(update_baptism_date_sql, update_baptism_date_values)

        db.commit()
    except Exception as e:
        print(f"Error in update_student: {e}")



# Delete a student record
def delete_student(student_id):
    sql = "DELETE FROM students WHERE id = ?"
    values = (student_id,)
    cursor.execute(sql, values)
    db.commit()

if __name__ == "__main__":
    create_table()
