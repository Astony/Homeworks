from django.db import models


class Person(models.Model):
    """Create table with person's name and surname in db"""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + self.last_name


class Student(Person):
    """Create table Student in db"""


class Teacher(Person):
    """Create table Teacher in db"""


class Homework(models.Model):
    """Create table Homework in db"""

    task = models.TextField()
    creator = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task


class HomeworkResult(models.Model):
    """Create table HomeworkResult in db"""

    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution = models.TextField()
    creator = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.solution
