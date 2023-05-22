from django.db import models
from django.contrib.auth.models import User
import uuid
from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin,AbstractBaseUser

from django.conf import settings
from django.utils.translation import gettext as _# Create your models here
import requests
import json
from django.core.files.storage import FileSystemStorage
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.db import models
from appRealestate.utils import path_file_name 

class UserAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,email,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        email = email.lower()
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,first_name,last_name, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    

class UserAccount(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True,max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    def __str__(self):
        return self.email





# class User(AbstractUser):
#     email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
# class EmailVerification(models.Model):
#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#         related_query_name="verification"
#     )
#     email_verified = models.BooleanField(default=False)
#     phone_number = models.CharField(max_length=50,null=True,blank=True)
#     # USERNAME_FIELD = 'email'
#     # REQUIRED_FIELDS = ['username']
    
class Profile(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    # user = models.OneToOneField(User, on_delete=models.CASCADE )
    name= models.CharField(max_length=255)
    username= models.CharField(max_length=200,blank=True,null=True)
    email= models.CharField(max_length=200,null=True,blank=True)
    # rating = models.IntegerField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # id = models.UUIDField(unique=True,default=uuid.uuid4,editable=False)
    def __str__(self):
        return self.user.username
    # class Meta:
    #     abstract = True

    
class Image(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    file = models.FileField(upload_to=path_file_name)

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"