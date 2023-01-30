from django.db import models

# Create your models here.


class Student(models.Model):
    ID = models.IntegerField(primary_key = True )
    Name = models.CharField(max_length=50)
    GPA = models.FloatField()
    level = models.IntegerField()
    mail = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    dep = models.CharField(max_length=2, blank=True)
    Gender = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    birth = models.DateField()
    
   