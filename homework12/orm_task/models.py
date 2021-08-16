from django.db import models


class Student(models.Model):
    """Create table Student in db"""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Teacher(models.Model):
    """Create table Teacher in db"""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Homework(models.Model):
    """Create table Homework in db"""

    task = models.TextField()
    creator = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)


class HomeworkResult(models.Model):
    """Create table HomeworkResult in db"""

    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution = models.TextField()
    creator = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
