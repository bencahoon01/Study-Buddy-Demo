# test_models.py
import unittest
from models import Course, AvailabilitySlot, User, StudySession


class TestCourse(unittest.TestCase):
    def test_course_creation(self):
        course = Course("CPSC2120")
        self.assertEqual(course.code, "CPSC2120")


class TestAvailabilitySlot(unittest.TestCase):
    def test_availability_slot_creation(self):
        slot = AvailabilitySlot("Monday", 14)
        self.assertEqual(slot.day, "Monday")
        self.assertEqual(slot.time, 14)

    def test_availability_slot_str(self):
        slot = AvailabilitySlot("Tuesday", 16)
        self.assertEqual(str(slot), "Tuesday at 16:00")


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("student", "password", "clemson student")

    def test_user_creation(self):
        self.assertEqual(self.user.username, "student")
        self.assertEqual(self.user.name, "clemson student")
        self.assertEqual(self.user.courses, [])
        self.assertEqual(self.user.availability, [])

    def test_add_course(self):
        self.user.add_course("MATH1080")
        self.assertEqual(len(self.user.courses), 1)
        self.assertEqual(self.user.courses[0].code, "MATH1080")

    def test_set_availability(self):
        self.user.set_availability("Tuesday", 16)
        self.assertEqual(len(self.user.availability), 1)
        slot = self.user.availability[0]
        self.assertEqual(slot.day, "Tuesday")
        self.assertEqual(slot.time, 16)


class TestStudySession(unittest.TestCase):
    def setUp(self):
        self.course = Course("CPSC2120")
        self.slot = AvailabilitySlot("Monday", 14)
        self.organizer = User("alice", "pw1", "Alice")
        self.invitee = User("bob", "pw2", "Bob")
        self.session = StudySession(self.course, self.slot, self.organizer, self.invitee)

    def test_study_session_creation(self):
        self.assertEqual(self.session.status, "Pending")
        self.assertEqual(self.session.course, self.course)
        self.assertEqual(self.session.slot, self.slot)
        self.assertEqual(self.session.organizer, self.organizer)
        self.assertEqual(self.session.invitee, self.invitee)

    def test_confirm_session(self):
        self.session.confirm()
        self.assertEqual(self.session.status, "Confirmed")

    def test_decline_session(self):
        self.session.decline()
        self.assertEqual(self.session.status, "Declined")


if __name__ == "__main__":
    unittest.main()
