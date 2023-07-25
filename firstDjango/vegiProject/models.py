from django.db import models

# Create your models here.

class receipe(models.Model):

    dishName = models.CharField(max_length=100)
    dishReceipe = models.TextField()
    dishImg = models.ImageField(upload_to="dishImg")