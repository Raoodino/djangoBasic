from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    #loading media files
    photo = models.ImageField(upload_to='images')
    designation = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100, unique = True)
    #blank = True -- optional
    phone_number = models.CharField(max_length=12, blank = True)
    #store initially created time
    #one-time modification -- only when the model instance is created/saved for the first time
    created_at = models.DateTimeField(auto_now_add=True)
    #store previously modified time -- current time whenever it is saved
    updated_at = models.DateTimeField(auto_now=True)
    
    # to present the employee using its first name
    def __str__(self):
        return self.first_name