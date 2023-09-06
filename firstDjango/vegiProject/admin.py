from django.contrib import admin
from .models import *
# Register your models here.
# `admin.site.register("register")` is registering the model "register" with the Django admin site.
# This allows the model to be managed and displayed in the admin interface.
admin.site.register(receipe)