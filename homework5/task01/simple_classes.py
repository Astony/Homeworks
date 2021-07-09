from datetime import datetime, timedelta


class Homework:
    """
    Class Homework that contains information about task,
    day to finish it, data of creating and information about deadline
    """

    def __init__(self, task: str, days: int):
        self.task = task
        self.days = days
        self.created = datetime.now()
        self.deadline = self.created + timedelta(days=days) - datetime.now()

    def is_active(self) -> bool:
        return self.deadline != timedelta()


class Student:
    """
    Class Student contains information about student and also have method to check
    if managed student do homework or not
    """

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, homework):
        if homework.is_active():
            return homework
        else:
            print("You are late")
            return None


class Teacher:
    """
    Class Teacher contains info about teacher and have method to create homework
    """

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def create_homework(self, task, days):
        return Homework(task, days)
