import unittest
from database import Session, Student

class TestDatabase(unittest.TestCase):
    def test_add_student(self):
        session = Session()
        student = Student(first_name='John', last_name='Doe', email='john.doe@example.com')
        session.add(student)
        session.commit()
        self.assertIsNotNone(student.id)

# More test cases...
