from django.db import models

# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=40)
    details = models.CharField(max_length=3000)
    course_price = models.IntegerField()
    course_duration = models.IntegerField()
    tutor = models.CharField(max_length=50)
    tutor_code = models.CharField(max_length=10)
    course_code = models.CharField(max_length=10,primary_key=True)

class Trainer(models.Model):
    trainer_name = models.CharField(max_length=50)
    trainer_code = models.CharField(max_length=10)


