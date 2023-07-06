from django.db import models

# Create your models here.
class StudentTable(models.Model):
    firstName = models.CharField(max_length=20)
    lastName  = models.CharField(max_length = 22)
    mobNumber = models.IntegerField()
    emailID   = models.EmailField()
    # imageFile = models.ImageField()
    age       = models.IntegerField()



class product(models.Model):
    pass