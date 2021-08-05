from datetime import datetime, timedelta
from typing import ClassVar, Type


class InvalidError(Exception):
    """This is my personal error for check_homework_type method"""


def check_homework_type(some_obj: ClassVar, homework_class: Type) -> "Homework":
    if isinstance(some_obj, homework_class):
        return some_obj
    else:
        raise InvalidError("Argument should has Homeworks class type")


class DeadlineError(Exception):
    """This is my personal error for do_homework method"""


class Homework:
    """
    Class Homework that contains information about task,
    day of finish it, data of creating and information about deadline.

    :param task: Text of task that should be done in the homework.
    :type task: str
    :param days: This argument represents how much time available to do this homework.
    :type days: int
    """

    def __init__(self, task: str, days: int) -> None:
        self.task = task
        self.created = datetime.now()
        self.deadline = self.created + timedelta(days=days) - datetime.now()

    def is_active(self) -> bool:
        """Returns True of False depending on time of deadline of this

        :return: Status of the homework
        :rtype: bool
        """
        return self.deadline > timedelta(days=0)


class Person:
    """Base class for students and teachers

    :param first_name: The first name of person.
    :type first_name: str
    :param last_name: The second name of person.
    :type last_name: str
    """

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):
    """
    Class Student contains information about student and also have method to check
    if managed student do homework or not. Class has as same attributes as :class: `Person` has.
    """

    def do_homework(self, homework_obj: Homework, solution: str) -> "HomeworkResult":
        """This method allows for instance of :class:`Student` to do a created homework

        :param homework: Some :class:`Homework` instance
        :return: :class:`HomeworkResult` instance or raise :class:`DeadlineError`
        """
        if check_homework_type(homework_obj, Homework) and homework_obj.is_active():
            return HomeworkResult(self, homework_obj, solution)
        else:
            raise DeadlineError("You are late")


class HomeworkResult:
    """Class that contains information about author(student) homework and solution

    :param student: an instance of :class:`Student` class.
    :type student: :class:`Student.
    :param homework_obj: an instance of :class:`Homework` class.
    :type homework_obj: :class:`Homework.
    :param solution: solution of given task.
    :type solution: str
    """

    def __init__(self, student: Student, homework_obj: Homework, solution: str) -> None:
        self.homework = check_homework_type(homework_obj, Homework)
        self.student = student
        self.solution = solution
        self.created = datetime.now()


class Teacher(Person):
    """
    Class Teacher contains info about teacher and have method to create homework and also
    here is the dictionary with all homeworks that have done and with their solutions.
    Class has as same attributes as :class: `Person` has.
    """

    homework_done = {}

    @staticmethod
    def create_homework(task: str, days: int) -> Homework:
        """This method creates a :class:`Homework` instance

        :param task: Text of task that should be done in the homework.
        :type task: str
        :param days: This argument represents how much time available to do this homework.
        :type days: int
        :return: :class:`Homework` instance
        """
        return Homework(task, days)

    @staticmethod
    def check_homework(homework_result_obj: HomeworkResult) -> bool:
        """This method check a :class:`HomeworkResult` instance.

        :param homework_result_obj: an instance of :class:`HomeworkResult` class.
        :type homework_result_obj: :class:`HomeworkResult`
        :return: True if len of solution > 5 and False instead.
        :rtype: bool
        """
        if len(homework_result_obj.solution) > 5:
            Teacher.homework_done[homework_result_obj] = homework_result_obj.solution
            return True
        return False

    @staticmethod
    def reset_results(homework_result: HomeworkResult = None) -> None:
        """This method reset dictionary with completed homeworks if it using without arguments
         or deletes element that gives as attribute.

        :param homework_result_obj: an instance of :class:`HomeworkResult` class.
        :type homework_result_obj: :class:`HomeworkResult`
        """
        if homework_result:
            del Teacher.homework_done[homework_result]
        else:
            Teacher.homework_done.clear()
