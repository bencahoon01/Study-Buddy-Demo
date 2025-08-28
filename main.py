import sys
from PyQt6.QtWidgets import QApplication
from controller import StudyBuddyController
from view import MainWindow


def main():
    app = QApplication(sys.argv)

    # Controller (logic + state)
    controller = StudyBuddyController()

    # View (PyQt window)
    window = MainWindow(controller)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
