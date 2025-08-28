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
        # Find current user's availability and courses
        current_user_availability = self.current_user.availability

        for user in self.users.values():
            if user.username == self.current_user.username:
                continue

            # Check if user is in the target course
            is_enrolled = any(c.code == target_course_code for c in user.courses)

            if is_enrolled:
                # Check for overlapping availability
                for my_slot in current_user_availability:
                    is_overlap = any(o.day == my_slot.day and o.time == my_slot.time for o in user.availability)
                    if is_overlap:
                        matches.append(user)
                        break
        return matches

    def schedule_session(self):
        p_user, c_code, day, time = self.view.get_session_details()

        # Validations
        if p_user not in self.users:
            self.view.display_message("Partner username not found.")
            return

        invitee = self.users[p_user]

        # Create session object
        course = models.Course(c_code)
        slot = models.AvailabilitySlot(day, time)
        session = models.StudySession(course, slot, self.current_user, invitee)
        self.sessions.append(session)
        self.view.display_message(f"Invitation sent to {p_user}.")

    def manage_sessions(self):
        user_sessions = [s for s in self.sessions if s.organizer == self.current_user or s.invitee == self.current_user]
        self.view.display_sessions(user_sessions, self.current_user.username)

        pending_invites = [s for s in user_sessions if s.invitee == self.current_user and s.status == "Pending"]

        if pending_invites:
            if input("\nManage pending invitations? (y/n): ").lower() == 'y':
                index, action = self.view.get_session_confirmation_choice()
                # Find the actual session object to update
                session_to_manage = user_sessions[index]
                if session_to_manage.invitee == self.current_user and session_to_manage.status == "Pending":
                    if action == 'confirm':
                        session_to_manage.confirm()
                        self.view.display_message("Session confirmed.")
                    elif action == 'decline':
                        session_to_manage.decline()
                        self.view.display_message("Session declined.")
                else:
                    self.view.display_message("Invalid selection.")