# main.py
# --- Entry point of the application ---

import controller


def main():
    """Initializes the controller and starts the main application loop."""
    app_controller = controller.StudyBuddyController()
    app_controller.run()


if __name__ == "__main__":
    main()




