import pytest

from homework12.orm.models import Homework, HomeworkResult, Student, Teacher


def create_record_in_db(some_class, **kwargs):
    """Function for creation record in db"""
    instance = some_class(**kwargs)
    instance.save()
    return instance


@pytest.fixture
def create_tables():
    "The fixture creates tables before running tests"
    teacher = create_record_in_db(Teacher, first_name="John", last_name="Wick")
    homework = create_record_in_db(Homework, task="databases", creator=teacher)
    student = create_record_in_db(Student, first_name="Joe", last_name="Baiden")
    hw_result = create_record_in_db(
        HomeworkResult, homework=homework, solution="abacaba", creator=student
    )
    yield
