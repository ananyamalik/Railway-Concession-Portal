from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
# Create your models here.

"""def upload_location(instance, filename):
    return "profiles/{filename}".format(filename=filename)"""

class StudentProfile(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255,blank=False)
    profile_pic = models.ImageField(upload_to='profile_pic/', blank=True)
    aadhar = models.FileField(upload_to='aadhar/',blank=True)
    startstation = models.CharField(max_length=10)
    endstation = models.CharField(max_length=10)
    pass_out = models.CharField(max_length=4)
    department = models.CharField(max_length=50)
    issued = models.BooleanField(default=False)
    date_of_issue = models.DateTimeField(default=datetime.now())

    def __str__(self):
        #name = first_name+last_name
        return self.first_name
