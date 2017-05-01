
'''
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	Created = models.DateTimeField(auto_now_add=True)
	major = models.TextField(max_length=100,blank=True)
	province = models.TextField(max_length=100,blank=True)
	school = models.TextField(max_length=100,blank=True)
	city = TextField(max_length=100,blank=True)

@receiver(post_save,sender=User)
def create_profile(sender,instance,**kwargs):
	if Created:
		Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
	instance.profile.save()
'''
