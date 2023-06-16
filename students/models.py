from django.db import models

# Create your models here.


class Studentmodel(models.Model):
    student_id = models.IntegerField()
    name = models.CharField(max_length=220)
    age = models.IntegerField()
    gender = models.CharField(max_length=220)
    email = models.EmailField()
    classs = models.CharField(max_length=220)
