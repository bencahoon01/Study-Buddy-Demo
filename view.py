from PyQt6.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMainWindow, QMessageBox
)
class CLIView:
    def __init__(self):
        print("CLIView initialized")
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class StudyBuddyView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Study Buddy')
        layout = QVBoxLayout()
        label = QLabel('Welcome to Study Buddy!')
        layout.addWidget(label)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("StudyBuddy")
        self.setGeometry(200, 200, 400, 300)

        self.login_widget = LoginWidget(controller, self)
        self.setCentralWidget(self.login_widget)


class LoginWidget(QWidget):
    def __init__(self, controller, main_window):
        super().__init__()
        self.controller = controller
        self.main_window = main_window

        self.layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.handle_login)

        self.create_button = QPushButton("Create Profile")
        self.create_button.clicked.connect(self.handle_create_profile)

        self.layout.addWidget(QLabel("Welcome to StudyBuddy!"))
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.login_button)
        self.layout.addWidget(self.create_button)

        self.setLayout(self.layout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        user = self.controller.users.get(username)

        if user and user.password == password:
            self.controller.current_user = user
            QMessageBox.information(self, "Login", f"Welcome, {user.name}!")
            self.main_window.setCentralWidget(MainMenu(self.controller, self.main_window))
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password.")

    def handle_create_profile(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if username in self.controller.users:
            QMessageBox.warning(self, "Error", "Username already exists.")
        else:
            from models import User
            self.controller.users[username] = User(username, password, username)
            QMessageBox.information(self, "Profile", "Profile created successfully!")


class MainMenu(QWidget):
    def __init__(self, controller, main_window):
        super().__init__()
        self.controller = controller
        self.main_window = main_window

        self.layout = QVBoxLayout()

        self.layout.addWidget(QLabel(f"Logged in as: {controller.current_user.name}"))

        self.course_button = QPushButton("Manage Courses")
        self.avail_button = QPushButton("Manage Availability")
        self.partner_button = QPushButton("Find Partner")
        self.session_button = QPushButton("Manage Sessions")
        self.logout_button = QPushButton("Logout")

        self.logout_button.clicked.connect(self.handle_logout)

        self.layout.addWidget(self.course_button)
        self.layout.addWidget(self.avail_button)
        self.layout.addWidget(self.partner_button)
        self.layout.addWidget(self.session_button)
        self.layout.addWidget(self.logout_button)

        self.setLayout(self.layout)

    def handle_logout(self):
        self.controller.current_user = None
        self.main_window.setCentralWidget(LoginWidget(self.controller, self.main_window))


from PyQt6.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMessageBox, QHBoxLayout
)


class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("StudyBuddy")
        self.setGeometry(200, 200, 400, 300)

        self.setCentralWidget(LoginWidget(controller, self))


# ----------------- LOGIN -----------------
class LoginWidget(QWidget):
    def __init__(self, controller, main_window):
        super().__init__()
        self.controller = controller
        self.main_window = main_window

        self.layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.handle_login)

        self.create_button = QPushButton("Create Profile")
        self.create_button.clicked.connect(self.handle_create_profile)

        self.layout.addWidget(QLabel("Welcome to StudyBuddy!"))
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.login_button)
        self.layout.addWidget(self.create_button)

        self.setLayout(self.layout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        user = self.controller.users.get(username)

        if user and user.password == password:
            self.controller.current_user = user
            QMessageBox.information(self, "Login", f"Welcome, {user.name}!")
            self.main_window.setCentralWidget(MainMenu(self.controller, self.main_window))
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password.")

    def handle_create_profile(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if username in self.controller.users:
            QMessageBox.warning(self, "Error", "Username already exists.")
        else:
            from models import User
            self.controller.users[username] = User(username, password, username)
            QMessageBox.information(self, "Profile", "Profile created successfully!")


# ----------------- MAIN MENU -----------------
class MainMenu(QWidget):
    def __init__(self, controller, main_window):
        super().__init__()
        self.controller = controller
        self.main_window = main_window

        layout = QVBoxLayout()

        layout.addWidget(QLabel(f"Logged in as: {controller.current_user.name}"))

        self.course_button = QPushButton("Manage Courses")
        self.course_button.clicked.connect(self.show_courses)

        self.avail_button = QPushButton("Manage Availability")
        self.avail_button.clicked.connect(self.show_availability)

        self.partner_button = QPushButton("Find Partner")
        self.partner_button.clicked.connect(self.show_partners)

        self.session_button = QPushButton("Manage Sessions")
        self.session_button.clicked.connect(self.show_sessions)

        self.logout_button = QPushButton("Logout")
        self.logout_button.clicked.connect(self.handle_logout)

        layout.addWidget(self.course_button)
        layout.addWidget(self.avail_button)
        layout.addWidget(self.partner_button)
        layout.addWidget(self.session_button)
        layout.addWidget(self.logout_button)

        self.setLayout(layout)

    def show_courses(self):
        self.main_window.setCentralWidget(CoursePage(self.controller, self.main_window))

    def show_availability(self):
        self.main_window.setCentralWidget(AvailabilityPage(self.controller, self.main_window))

    def show_partners(self):
        self.main_window.setCentralWidget(PartnerPage(self.controller, self.main_window))

    def show_sessions(self):
        self.main_window.setCentralWidget(SessionPage(self.controller, self.main_window))

    def handle_logout(self):
        self.controller.current_user = None
        self.main_window.setCentralWidget(LoginWidget(self.controller, self.main_window))


# ----------------- PAGES -----------------
class CoursePage(QWidget):
    def __init__(self, controller, main_window):
        super().__init__()
        self.controller = controller
        self.main_window = main_window

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Manage Courses"))

        self.course_input = QLineEdit()
        self.course_input.setPlaceholderText("Enter course code")
        layout.addWidget(self.course_input)

        add_button = QPushButton("Add Course")
        add_button.clicked.connect(self.add_course)
        layout.addWidget(add_button)

        back_button = QPushButton("Back to Menu")
        back_button.clicked.connect(self.go_back)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def add_course(self):
        code = self.course_input.text()
        self.controller.current_user.add_course(code)
        QMessageBox.information(self, "Course", f"Course {code} added!")

    def go_back(self):
        self.main_window.setCentralWidget(MainMenu(self.controller, self.main_window))


class AvailabilityPage(QWidget):
    def __init__(self, controller, main_window):
        super().__init__()
        self.controller = controller
        self.main_window = main_window

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Manage Availability"))

        self.day_input = QLineEdit()
        self.day_input.setPlaceholderText("Day (e.g., Monday)")
        layout.addWidget(self.day_input)

        self.time_input = QLineEdit()
        self.time_input.setPlaceholderText("Time (24h format, e.g., 14)")
        layout.addWidget(self.time_input)

        add_button = QPushButton("Add Availability")
        add_button.clicked.connect(self.add_availability)
        layout.addWidget(add_button)

        back_button = QPushButton("Back to Menu")
        back_button.clicked.connect(self.go_back)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def add_availability(self):
        day = self.day_input.text()
        try:
            time = int(self.time_input.text())
            self.controller.current_user.set_availability(day, time)
            QMessageBox.information(self, "Availability", f"Added {day} at {time}:00")
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter a valid hour (0-23).")

    def go_back(self):
        self.main_window.setCentralWidget(MainMenu(self.controller, self.main_window))


class PartnerPage(QWidget):
    def __init__(self, controller, main_window):
        super().__init__()
        self.controller = controller
        self.main_window = main_window

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Find a Study Partner (coming soon)"))

        back_button = QPushButton("Back to Menu")
        back_button.clicked.connect(self.go_back)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def go_back(self):
        self.main_window.setCentralWidget(MainMenu(self.controller, self.main_window))


class SessionPage(QWidget):
    def __init__(self, controller, main_window):
        super().__init__()
        self.controller = controller
        self.main_window = main_window

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Manage Sessions (coming soon)"))

        back_button = QPushButton("Back to Menu")
        back_button.clicked.connect(self.go_back)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def go_back(self):
        self.main_window.setCentralWidget(MainMenu(self.controller, self.main_window))
