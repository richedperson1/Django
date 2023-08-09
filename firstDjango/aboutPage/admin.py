from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(StudentTable)
admin.site.register(parentInfo)