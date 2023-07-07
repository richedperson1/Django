from django.db import models

# Create your models here.
# Python manage.py makemigrations

# Create your models here.
class StudentTable(models.Model):
    firstName = models.CharField(max_length=23)
    lastName  = models.CharField(max_length = 23)
    mobNumber = models.IntegerField()
    emailID   = models.EmailField()
    # imageFile = models.ImageField()
    age       = models.IntegerField()