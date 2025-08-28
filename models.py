# -----------------------------------------------------------------

# models.py
# --- Contains all data classes for the application ---

from typing import List


class Course:
    def __init__(self, code: str):
        self.code = code


class AvailabilitySlot:
    def __init__(self, day: str, time: int):
        self.day = day
        self.time = time  # e.g., 14 for 2 PM

    def __str__(self):
        return f"{self.day} at {self.time}:00"


class User:
    def __init__(self, username: str, password: str, name: str):
        self.username = username
        self.password = password
        self.name = name
        self.courses: List[Course] = []
        self.availability: List[AvailabilitySlot] = []

    def add_course(self, course_code: str):
        self.courses.append(Course(course_code))

    def set_availability(self, day: str, time: int):
        self.availability.append(AvailabilitySlot(day, time))


class StudySession:
    def __init__(self, course: Course, slot: AvailabilitySlot, organizer: User, invitee: User):
        self.course = course
        self.slot = slot
        self.organizer = organizer
        self.invitee = invitee
        self.status = "Pending"  # Status can be Pending, Confirmed, Declined

    def confirm(self):
        self.status = "Confirmed"

    def decline(self):
        self.status = "Declined"

