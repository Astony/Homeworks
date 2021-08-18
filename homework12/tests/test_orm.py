import pytest

from homework12.project.orm.models import Homework, HomeworkResult, Student, Teacher


@pytest.mark.parametrize(
    "record, result",
    [
        ("teacher.first_name", "John"),
        ("homework.creator.first_name", "John"),
        ("student.first_name", "Joe"),
        ("hw_result.creator.first_name", "Joe"),
    ],
)
@pytest.mark.django_db
def test_positive_cases(create_tables, record, result):
    """Test that all created records exist in test db"""

    teacher = Teacher.objects.get(first_name="John")
    homework = Homework.objects.get(creator=teacher.id)
    student = Student.objects.get(first_name="Joe")
    hw_result = HomeworkResult.objects.get(creator=student.id)
    assert eval(record) == result


@pytest.mark.django_db
def test_negative_case(create_tables):
    """Test that attempt to get an empty query throw an exception"""
    with pytest.raises(Exception):
        teacher = Teacher.objects.get(first_name="Incognito")
        assert not teacher.first_name == "Incognito"
