from datetime import datetime, timedelta
from typing import ClassVar

from homework6.task02.check_homework_type import check_homework_type


class DeadlineError(Exception):
    """This is my personal error for do_homework method"""


class Homework:
    """
    Class Homework that contains information about task,
    day of finish it, data of creating and information about deadline
    """

    def __init__(self, task: str, days: int) -> None:
        self.task = task
        self.days = days
        self.created = datetime.now()
        self.deadline = self.created + timedelta(days=days) - datetime.now()

    def is_active(self) -> bool:
        return self.deadline > timedelta(days=0)


class HomeworkResult:
    """Class that contains information about author(student) homework and solution"""

    def __init__(
        self, student: ClassVar, homework_obj: ClassVar, solution: str
    ) -> None:
        self.student = student
        self.solution = solution
        self.created = datetime.now()
        if check_homework_type(homework_obj, Homework):
            self.homework = homework_obj


class Person:
    """Base class for students and teachers"""

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):
    """
    Class Student contains information about student and also have method to check
    if managed student do homework or not
    """

    def do_homework(self, homework_obj: ClassVar, solution: str) -> ClassVar:
        if check_homework_type(homework_obj, Homework) and homework_obj.is_active():
            return HomeworkResult(self, homework_obj, solution)
        else:
            raise DeadlineError("You are late")


class Teacher(Person):
    """
    Class Teacher contains info about teacher and have method to create homework and also
    here is the dictionary with all homeworks that have done and with their solutions.
    """

    homework_done = {}

    def create_homework(self, task: str, days: int) -> ClassVar:
        return Homework(task, days)

    def check_homework(self, homework_result_obj: ClassVar) -> bool:
        if len(homework_result_obj.solution) > 5:
            Teacher.homework_done[homework_result_obj] = homework_result_obj.solution
            return True
        return False

    def reset_results(self, *args: ClassVar) -> None:
        if args:
            if len(args) == 1 and isinstance(args[0], HomeworkResult):
                del Teacher.homework_done[args[0]]
        else:
            Teacher.homework_done.clear()
