# from django.db.models.signals import pre_save, post_save
# from django.shortcuts import get_object_or_404
# from django.dispatch import receiver

# from .models import Profile,User


 
# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     print("post save profile")
#     if created:
#         Profile.objects.create(user=instance)
  
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#         instance.profile.save()