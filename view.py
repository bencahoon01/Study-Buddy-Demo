from PyQt6.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QListWidget,
    QMessageBox, QHBoxLayout, QInputDialog, QMainWindow
)
import models

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


class PartnerPage(QWidget):
    def __init__(self, controller, main_window):
        super().__init__()
        self.controller = controller
        self.main_window = main_window

        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("Find a Study Partner"))

        self.course_input = QLineEdit()
        self.course_input.setPlaceholderText("Enter course code")
        self.layout.addWidget(self.course_input)

        self.search_button = QPushButton("Find Partners")
        self.search_button.clicked.connect(self.find_partners)
        self.layout.addWidget(self.search_button)

        self.matches_list = QListWidget()
        self.layout.addWidget(self.matches_list)

        self.invite_button = QPushButton("Invite Selected Partner")
        self.invite_button.clicked.connect(self.invite_partner)
        self.layout.addWidget(self.invite_button)

        back_button = QPushButton("Back to Menu")
        back_button.clicked.connect(self.go_back)
        self.layout.addWidget(back_button)

        self.setLayout(self.layout)

    def find_partners(self):
        course_code = self.course_input.text()
        matches = self.controller._suggest_matches(course_code)

        self.matches_list.clear()
        if not matches:
            self.matches_list.addItem("No partners found.")
            return

        for u in matches:
            self.matches_list.addItem(f"{u.username} ({u.name})")

    def invite_partner(self):
        selected = self.matches_list.currentItem()
        if not selected or "No partners" in selected.text():
            QMessageBox.warning(self, "Error", "Please select a valid partner.")
            return

        partner_username = selected.text().split(" ")[0]
        course_code = self.course_input.text()

        # Ask for slot details
        day, ok1 = QInputDialog.getText(self, "Day", "Enter day (e.g., Monday):")
        if not ok1:
            return
        time, ok2 = QInputDialog.getInt(self, "Time", "Enter hour (0-23):", min=0, max=23)
        if not ok2:
            return

        # Schedule session
        course = models.Course(course_code)
        slot = models.AvailabilitySlot(day, time)
        partner = self.controller.users.get(partner_username)

        if not partner:
            QMessageBox.warning(self, "Error", "Partner not found.")
            return

        session = models.StudySession(course, slot, self.controller.current_user, partner)
        self.controller.sessions.append(session)
        QMessageBox.information(self, "Session", f"Invitation sent to {partner_username}!")

    def go_back(self):
        from view import MainMenu
        self.main_window.setCentralWidget(MainMenu(self.controller, self.main_window))


class SessionPage(QWidget):
    def __init__(self, controller, main_window):
        super().__init__()
        self.controller = controller
        self.main_window = main_window

        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("Manage Sessions"))

        self.sessions_list = QListWidget()
        self.layout.addWidget(self.sessions_list)

        self.confirm_button = QPushButton("Confirm Invitation")
        self.confirm_button.clicked.connect(self.confirm_invite)
        self.layout.addWidget(self.confirm_button)

        self.decline_button = QPushButton("Decline Invitation")
        self.decline_button.clicked.connect(self.decline_invite)
        self.layout.addWidget(self.decline_button)

        back_button = QPushButton("Back to Menu")
        back_button.clicked.connect(self.go_back)
        self.layout.addWidget(back_button)

        self.setLayout(self.layout)
        self.refresh_sessions()

    def refresh_sessions(self):
        self.sessions_list.clear()
        user_sessions = [
            s for s in self.controller.sessions
            if s.organizer == self.controller.current_user or s.invitee == self.controller.current_user
        ]

        if not user_sessions:
            self.sessions_list.addItem("No sessions found.")
            return

        for idx, s in enumerate(user_sessions):
            role = "Organizer" if s.organizer == self.controller.current_user else "Invitee"
            self.sessions_list.addItem(
                f"{idx}: {s.course} on {s.slot} | {s.organizer.name} → {s.invitee.name} "
                f"[{s.status}] ({role})"
            )

    def get_selected_session(self):
        selected = self.sessions_list.currentItem()
        if not selected or "No sessions" in selected.text():
            return None
        idx = int(selected.text().split(":")[0])
        user_sessions = [
            s for s in self.controller.sessions
            if s.organizer == self.controller.current_user or s.invitee == self.controller.current_user
        ]
        return user_sessions[idx]

    def confirm_invite(self):
        session = self.get_selected_session()
        if session and session.invitee == self.controller.current_user and session.status == "Pending":
            session.confirm()
            QMessageBox.information(self, "Session", "Invitation confirmed!")
            self.refresh_sessions()
        else:
            QMessageBox.warning(self, "Error", "Please select a valid pending invite.")

    def decline_invite(self):
        session = self.get_selected_session()
        if session and session.invitee == self.controller.current_user and session.status == "Pending":
            session.decline()
            QMessageBox.information(self, "Session", "Invitation declined.")
            self.refresh_sessions()
        else:
            QMessageBox.warning(self, "Error", "Please select a valid pending invite.")

    def go_back(self):
        from view import MainMenu
        self.main_window.setCentralWidget(MainMenu(self.controller, self.main_window))
