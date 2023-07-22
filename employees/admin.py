from django.contrib import admin
#from current directory import models.py
from .models import Employee
# Register your models here.
admin.site.register(Employee)