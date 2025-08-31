# controller.py
# --- Contains the main application logic and state ---

import models
import view


class StudyBuddyController:
    def __init__(self):
        self.users = {}  # In-memory user storage
        self.sessions = []  # In-memory session storage
        self.view = view.StudyBuddyView()
        self.current_user = None

    def run(self):
        self.view.display_welcome()
        while True:
            if not self.current_user:
                choice = self.view.display_login_menu()
                if choice == '1':
                    self.login()
                elif choice == '2':
                    self.create_profile()
                elif choice == '3':
                    break
            else:
                choice = self.view.display_main_menu()
                if choice == '1':
                    self.manage_courses()
                elif choice == '2':
                    self.manage_availability()
                elif choice == '3':
                    self.find_partner_flow()
                elif choice == '4':
                    self.manage_sessions()
                elif choice == '5':
                    self.logout()

    def create_profile(self):
        username, password, name = self.view.get_new_profile_info()
        if username in self.users:
            self.view.display_message("Username already exists.")
        else:
            self.users[username] = models.User(username, password, name)
            self.view.display_message("Profile created successfully! Please log in.")

    def login(self):
        username, password = self.view.get_user_credentials()
        user = self.users.get(username)
        if user and user.password == password:
            self.current_user = user
            self.view.display_message(f"Welcome, {self.current_user.name}!")
        else:
            self.view.display_message("Invalid username or password.")

    def logout(self):
        self.view.display_message(f"Goodbye, {self.current_user.name}!")
        self.current_user = None

    def manage_courses(self):
        code = self.view.get_course_code()
        self.current_user.add_course(code)
        self.view.display_message(f"Course {code} added.")

    def manage_availability(self):
        day, time = self.view.get_availability_slot()
        self.current_user.set_availability(day, time)
        self.view.display_message(f"Availability added for {day} at {time}:00.")

    def find_partner_flow(self):
        course_code = self.view.get_course_code()
        matches = self._suggest_matches(course_code)
        self.view.show_matches(matches)

        if matches:
            if input("Do you want to schedule a session? (y/n): ").lower() == 'y':
                self.schedule_session()

    def _suggest_matches(self, target_course_code):
        matches = []
        current_user_availability = self.current_user.availability

        for user in self.users.values():
            if user.username == self.current_user.username:
                continue

            is_enrolled = any(c.code == target_course_code for c in user.courses)

            if is_enrolled:
                for my_slot in current_user_availability:
                    is_overlap = any(o.day == my_slot.day and o.time == my_slot.time for o in user.availability)
                    if is_overlap:
                        matches.append(user)
                        break  # Only need one overlapping slot to match

        return matches
