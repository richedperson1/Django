from django.db import models

# Create your models here.
# The class "receipe" is a model in Python that represents a recipe with attributes such as dishName,
# dishReceipe, and dishImg.

class receipe(models.Model):
    dishName = models.CharField(max_length=100)
    dishReceipe = models.TextField()
    dishImg = models.ImageField(upload_to="dishImg")