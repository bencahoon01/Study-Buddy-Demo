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

if __name__ == "__main__":
    unittest.main()
