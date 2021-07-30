from datetime import datetime, timedelta
from typing import Any


class Homework:
    """This is a class that contains information about a created homework by a :class:`Teacher`.

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


class Student:
    """
    Class Student contains information about student and also have method to check
    if managed student do homework or not.

    :param first_name: The first name of student.
    :type first_name: str
    :param last_name: The second name of student.
    :type last_name: str

    """

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def do_homework(homework: Homework) -> Any:
        """This method allows for instance of :class:`Student` to do a created homework

        :param homework: Some :class:`Homework` instance
        :return: :class:`Homework` instance or None
        """
        if homework.is_active():
            return homework
        print("You are late")
        return None


class Teacher:
    """
    Class Teacher contains info about teacher and have method to create homework

    :param first_name: The first name of teacher.
    :type first_name: str
    :param last_name: The second name of teacher.
    :type last_name: str
    """

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

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
