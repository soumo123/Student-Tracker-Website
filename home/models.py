
from django.db import models
from django.contrib.auth.models import User

class Registration(models.Model):
    fullname = models.CharField(max_length=122)
    email =  models.CharField(max_length=122)
    mobile = models.CharField(max_length=122)
    stream = models.CharField(max_length=122)
    skills = models.CharField(max_length=122)
    experience = models.CharField(max_length=122)
    graduation = models.CharField(max_length=122)
    about = models.CharField(max_length=122)
    # img=models.ImageField(upload_to="profile_pics" ,default="profile_pics/untitled-1.jpg")
    verified = models.CharField(max_length=122,null=True)
    # date = models.DateField()
    class Meta():
        db_table="studentregistration"
    def __str__(self):
        return self.fullname

# class user(models.Model):
#     user=models.CharField(max_length=122)
#     image=models.ImageField(upload_to="profile_pics" ,default="profile_pics/untitled-1.jpg")
