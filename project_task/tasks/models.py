from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model):
    statuses = [
        ('Started', 'Started'),
        ('Ongoing', 'Ongoing'),
        ('Dropped', 'Dropped'),
        ('Completed', 'Completed'),
    ]
    users = [
        ('student 1', 'student 1'),
        ('student 2', 'student 2'),
        ('student 3', 'student 3'),
        ('student 4', 'student 4'),
        ('student 5', 'student 5'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default="Task Name")
    description = models.CharField(max_length=200)
    assign_to = models.CharField(max_length=100, choices=users)
    status = models.CharField(max_length=20, default='Started',choices=statuses)
    priority = models.CharField(max_length=20)
    deadline = models.DateField()
    remarks = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True)

class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class TaskUpdate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    remarks = models.TextField()
    last_updated = models.DateTimeField(auto_now_add=True)