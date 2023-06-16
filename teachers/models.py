from django.db import models

# Create your models here.


class Teachermodel(models.Model):
    teacher_id = models.IntegerField()
    name = models.CharField(max_length=220)
    gender = models.CharField(max_length=220)
    email = models.EmailField()
    subject = models.CharField(max_length=220)
