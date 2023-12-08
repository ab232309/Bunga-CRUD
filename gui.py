import sys
from PyQt5.QtWidgets import QApplication
from app_ui import StudentInformationSystem

def run_gui():
    app = QApplication(sys.argv)
    window = StudentInformationSystem()
    window.show()
    app.exec_()

if __name__ == "__main__":
    run_gui()
