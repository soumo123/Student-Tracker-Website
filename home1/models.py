from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    img=models.ImageField(default='images/civil.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}Profile'

# @receiver(post_save, sender=User)
# def update_profile_signal(sender,instance,created ,**kwargs):
#     if created:
#         UserProfile.objects.create( profile_user=instance)
#     instance.userprofile.save()
        
    
class Image(models.Model):
    caption=models.CharField(max_length=120)
    image=models.ImageField(upload_to="img/%y")
    def __str__(self):
        return self.caption

