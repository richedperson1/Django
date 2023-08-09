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
    
    
class parentInfo(models.Model):
    studentName = models.CharField(max_length=50,verbose_name="name of student those parent info need to save")
    fatherName = models.CharField(max_length=60,verbose_name="Student father name")
    motherName = models.CharField(max_length=60,verbose_name="Student mother name")
    mobileNumber = models.IntegerField(verbose_name="student guardian of number")
    occupations = models.CharField(max_length=20)