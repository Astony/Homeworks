import pytest

from homework6.task02.hard_classes_task import (DeadlineError, Homework,
                                                HomeworkResult, Student,
                                                Teacher)


class SomeClass:
    """This is additional class for test HomeworkResult class"""


good_student = Student("Billy", "Jean")
homework1 = Homework("Pot challenge", 5)
good_result = good_student.do_homework(homework1, "Make some pot")


def test_do_homework_method_positive_cases():
    """Check attributes of HomeworkResult"""
    assert good_result.student is good_student
    assert good_result.solution == "Make some pot"


bad_student = Student("Van", "Darkholm")
homework2 = Homework("Gym training", 0)


def test_do_homework_method_exception_case():
    """Checking new functionality of do_homework method"""
    with pytest.raises(DeadlineError, match="You are late"):
        bad_student.do_homework(homework2, "Training is completed master ")


some_object = SomeClass()


def test_HomeworkResult_wrong_type_of_input_attribute():
    """Checking that non-Homework type as an argument of do_homework raises error"""
    with pytest.raises(
        AttributeError, match="Argument should has Homeworks class type"
    ):
        good_student.do_homework(some_object, "I did something wrong, isn't it?")
    with pytest.raises(
        AttributeError, match="Argument should has Homeworks class type"
    ):
        HomeworkResult(good_student, some_object, "abacaba")


master_teacher = Teacher("Dzhan", "Yang")
another_teacher = Teacher("Mister", "Fox")


def test_inheritance_is_working():
    """Checking attributes Teacher's object after inheritance"""
    assert master_teacher.first_name == "Dzhan"


lazy_student = Student("Kick", "Buttovsky")
short_result = lazy_student.do_homework(homework1, "Done")
another_good_result = bad_student.do_homework(homework1, "I made the pot master")


def test_check_method_with_short_and_correct_solution():
    """Check the new teacher's method"""
    assert not master_teacher.check_homework(short_result)
    assert master_teacher.check_homework(good_result)


master_teacher.check_homework(good_result)
another_teacher.check_homework(another_good_result)


def test_dict_contain():
    """Check Teacher's dict content"""
    dict_element = Teacher.homework_done[good_result]
    assert len(master_teacher.homework_done.keys()) == 2
    assert dict_element == "Make some pot"


def test_reset_results_method():
    """Check reset results method with correct argument"""
    master_teacher.reset_results(good_result)
    assert len(master_teacher.homework_done) == 1
    assert list(another_teacher.homework_done.keys())[0] is another_good_result
    assert another_teacher.homework_done is master_teacher.homework_done


def test_full_reset():
    """Check reset results method without arguments"""
    master_teacher.reset_results()
    assert len(another_teacher.homework_done) == 0


def test_of_wrong_attributes_for_reset_method():
    """Check reset results method with incorrect arguments"""
    assert not master_teacher.reset_results(some_object, 5)
