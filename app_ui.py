import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QInputDialog
import main
import warnings

# Suppress the DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)

class StudentInformationSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Information System")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a table to display student records
        self.student_table = QTableWidget(self)
        self.student_table.setColumnCount(6)
        self.student_table.setHorizontalHeaderLabels(["Student ID", "Name", "Age", "Sign-up Date", "Lessons Listened","Baptism Date (est.)"])
        self.student_table.setEditTriggers(QTableWidget.DoubleClicked)

        # Create input fields
        self.name_label = QLabel("Name:")
        self.name_edit = QLineEdit()
        self.age_label = QLabel("Age:")
        self.age_edit = QLineEdit()
        self.signup_label = QLabel("Sign-up Date (YYYY-MM-DD):")
        self.signup_edit = QLineEdit()
        self.lessons_label = QLabel("Lessons Listened:")
        self.lessons_edit = QLineEdit()


        # Create buttons for CRUD operations
        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_student_button_clicked)
        self.update_button = QPushButton("Update")
        self.update_button.clicked.connect(self.update_student_button_clicked)
        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete_student_button_clicked)

        # Layout for input fields and buttons
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.name_label)
        input_layout.addWidget(self.name_edit)
        input_layout.addWidget(self.age_label)
        input_layout.addWidget(self.age_edit)
        input_layout.addWidget(self.signup_label)
        input_layout.addWidget(self.signup_edit)
        input_layout.addWidget(self.lessons_label)
        input_layout.addWidget(self.lessons_edit)
        input_layout.addWidget(self.create_button)
        input_layout.addWidget(self.update_button)
        input_layout.addWidget(self.delete_button)

        # Main layout
        layout = QVBoxLayout()
        layout.addWidget(self.student_table)
        layout.addLayout(input_layout)

        central_widget.setLayout(layout)

    def create_student_button_clicked(self):
        try:
            name = self.name_edit.text()
            age = int(self.age_edit.text())
            signup_date = self.signup_edit.text()
            lessons = int(self.lessons_edit.text())

            main.create_student(name, age, signup_date, lessons)
            self.update_student_table()

        except Exception as e:
            error_message = f"Error: {str(e)}"
            print(error_message)


    def update_student_button_clicked(self):
        selected_row = self.student_table.currentRow()
        if selected_row >= 0:
            student_id = self.student_table.item(selected_row, 0).text()
            updated_name = self.name_edit.text()
            updated_age = int(self.age_edit.text())
            updated_signup = input("Enter Updated Sign-up Date (YYYY-MM-DD): ") 
            updated_lessons = int(self.lessons_edit.text()) # Add this line

            main.update_student(student_id, updated_name, updated_age, updated_signup, updated_lessons)
            self.update_student_table()


    def delete_student_button_clicked(self):
        selected_row = self.student_table.currentRow()
        if selected_row >= 0:
            student_id = self.student_table.item(selected_row, 0).text()
            main.delete_student(student_id)
            self.update_student_table()

    def update_student_table(self):
        self.student_table.setRowCount(0)  # Clear the table
        students = main.read_students()

        for student in students:
            row_position = self.student_table.rowCount()
            self.student_table.insertRow(row_position)
            for i, field in enumerate(student):
                item = QTableWidgetItem(str(field))
                self.student_table.setItem(row_position, i, item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StudentInformationSystem()
    window.show()
    sys.exit(app.exec_())
