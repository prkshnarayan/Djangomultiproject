from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Student(models.Model):
    sales_person = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    date_of_joining = models.DateField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    age = models.IntegerField()
    place = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)

    class Meta:
        db_table = 'student'

    def __str__(self):
        return self.name
