# -----------------------------------------------------------------

# view.py
# --- Handles all command-line input and output ---

import getpass


class CLIView:
    def display_welcome(self):
        print("\n=== Welcome to the Clemson Study Buddy App! ===")

    def display_main_menu(self):
        print("\n--- Main Menu ---")
        print("1. Manage My Courses")
        print("2. Manage My Availability")
        print("3. Find a Study Partner")
        print("4. View My Study Sessions")
        print("5. Logout")
        return input("Choose an option: ")

    def display_login_menu(self):
        print("\n1. Login")
        print("2. Create a new profile")
        print("3. Exit")
        return input("Choose an option: ")

    def get_user_credentials(self):
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        return username, password

    def get_new_profile_info(self):
        username = input("Choose a username: ")
        password = getpass.getpass("Choose a password: ")
        name = input("Enter your full name: ")
        return username, password, name

    def get_course_code(self):
        return input("Enter course code (e.g., CPSC3720): ")

    def get_availability_slot(self):
        day = input("Enter day (e.g., Monday): ")
        time = int(input("Enter hour (24-hour format, e.g., 14 for 2 PM): "))
        return day, time

    def show_matches(self, matches):
        print("\n--- Potential Study Partners ---")
        if not matches:
            print("No matches found.")
        else:
            for user in matches:
                print(f"- {user.username}")

    def get_session_details(self):
        partner_username = input("Enter username of partner to schedule with: ")
        course_code = input("Enter course code: ")
        day = input("Enter day: ")
        time = int(input("Enter hour: "))
        return partner_username, course_code, day, time

    def display_sessions(self, sessions, current_username):
        print("\n--- My Study Sessions ---")
        if not sessions:
            print("You have no study sessions.")
            return

        for i, session in enumerate(sessions):
            if session.organizer.username == current_username:
                participant = session.invitee.username
                role = "Organizer"
            else:
                participant = session.organizer.username
                role = "Invitee"
            print(f"{i + 1}. With: {participant} | Course: {session.course.code} | "
                  f"When: {session.slot} | Status: {session.status} | Role: {role}")

    def get_session_confirmation_choice(self):
        session_index = int(input("Enter the number of the session to manage: ")) - 1
        action = input("Type 'confirm' or 'decline': ").lower()
        return session_index, action

    def display_message(self, message):
        print(f"\n[System] {message}")


