import pytest

from homework12.project.orm.models import Homework, HomeworkResult, Student, Teacher


@pytest.mark.django_db
def test_databases(create_tables):
    """Test that all created records exist in test db"""

    teacher = Teacher.objects.get(first_name="John")
    homework = Homework.objects.get(creator=teacher.id)
    student = Student.objects.get(first_name="Joe")
    hw_result = HomeworkResult.objects.get(creator=student.id)

    assert teacher.first_name == "John"
    assert homework.creator.first_name == "John"
    assert student.first_name == "Joe"
    assert hw_result.creator.first_name == "Joe"


@pytest.mark.django_db
def test_negative__db(create_tables):
    """Test that attempt to get an empty query throw an exception"""
    with pytest.raises(Exception):
        teacher = Teacher.objects.get(first_name="Incognito")
        assert not teacher.first_name == "Incognito"
