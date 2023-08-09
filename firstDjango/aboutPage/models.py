from django.db import models

# Create your models here.
# Python manage.py makemigrations

# Create your models here.
class StudentTable(models.Model):
    firstName = models.CharField(max_length=23)
    lastName  = models.CharField(max_length = 23)
    mobNumber = models.IntegerField(verbose_name="Mobile number of student")
    emailID   = models.EmailField(verbose_name = "Student Email ID")
    # imageFile = models.ImageField()
    age1       = models.IntegerField()
    age       = models.IntegerField()

    def __str__(self) -> str:
        return f"Name : {self.firstName}, Age : {self.age}"
    
    