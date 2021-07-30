from homework5.task01.simple_classes import Homework, Student, Teacher

teacher = Teacher("Daniil", "Shadrin")
student = Student("Roman", "Petrov")


def test_of_existing_student_and_teacher():
    """Check that teacher and students were created correctly"""
    assert teacher.first_name == "Daniil"
    assert student.first_name == "Roman"


expired_homework = teacher.create_homework("Learn functions", 0)


def test_of_homework_object():
    """Check homework object was created correctly"""
    assert expired_homework.task == "Learn functions"
    assert not expired_homework.is_active()


create_homework_too = teacher.create_homework
oop_homework = create_homework_too("create 2 simple classes", 5)


def test_creating_function_from_method():
    """Check the opportunity of teacher method to create homework object"""
    assert oop_homework.task == "create 2 simple classes"
    assert oop_homework.is_active()


def test_of_student_method(capsys):
    """Check student's method to do homework"""
    assert student.do_homework(oop_homework) is oop_homework
    assert student.do_homework(expired_homework) is None
    captured = capsys.readouterr()
    assert captured.out == "You are late\n"
