# student/models.py
from django.db import models
from django.utils import timezone

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    course = models.CharField(max_length=100)
    contact = models.CharField(max_length=20, null=True, blank=True)
    join_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name