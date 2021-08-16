from django.core.management import call_command
from django.test import TestCase

from orm_task.models import Homework, HomeworkResult, Student, Teacher


def create_record_in_db(some_class, **kwargs):
    """Function for creation record in db"""
    instance = some_class(**kwargs)
    instance.save()
    return instance


class DBTestCase(TestCase):
    def setUp(self):
        """Before run tests we make migrations in test db and create records into it"""
        call_command(("makemigrations"))
        call_command(("migrate"))
        teacher = create_record_in_db(Teacher, first_name="John", last_name="Wick")
        homework = create_record_in_db(Homework, task="databases", creator=teacher)
        student = create_record_in_db(Student, first_name="Joe", last_name="Baiden")
        hw_result = create_record_in_db(
            HomeworkResult, homework=homework, solution="abacaba", creator=student
        )

    def test_databases(self):
        """Test that all created records exist in test db"""
        teacher = Teacher.objects.get(first_name="John")
        homework = Homework.objects.get(creator=teacher.id)
        student = Student.objects.get(first_name="Joe")
        hw_result = HomeworkResult.objects.get(creator=student.id)
        self.assertEqual(teacher.first_name, "John")
        self.assertEqual(homework.creator.first_name, "John")
        self.assertEqual(student.first_name, "Joe")
        self.assertEqual(hw_result.creator.first_name, "Joe")
