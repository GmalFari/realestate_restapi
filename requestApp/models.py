from django.db import models

# Create your models here.
from django.urls import reverse
from django.db.models import Q
from django.contrib.gis.db import models as gis_models
from django.db.models.signals import pre_save,post_save
from django.utils.text import slugify
from django.db import models
from accounts.models import UserAccount
from smart_selects.db_fields import ChainedForeignKey 
from django.contrib.gis.geos import Point
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from appRealestate.utils import path_file_name , img_file_name, slugify_instance_company
class Req_order(models.Model):
    offer_choices = [
        ('for_rent','for rent'),
        ('for_sale','for sale')
    ]
    ownership_choices = [
        ('free','free'),
        ('waqf','waqf')
    ]
    type_choices = [
        ('dept','department'),
        ('house','house'),
        ('land','land'),
        ('basement','basement'),
    ]
    town_choices = [
        ('sanaa',"sana'a"),
        ('Dhamar','Dhamar'),
        ("Taiz","Taiz")
    ]
    rent_frequency_choices = [
        ('Daily','Daily'),
        ('Weekly','Weekly'),
        ('mounthly','mounthly'),
        ('Yearly','Yearly')
    ]
    owner = models.ForeignKey(UserAccount, null=True, blank=True, on_delete=models.SET_NULL)    
    req_order_slug = models.SlugField(null=True,blank=True) 
    req_order_title = models.CharField(max_length=250)
    purpose = models.CharField(max_length=20,null=True,blank=True) # للبيع للإيجار
    location = gis_models.PointField(srid=4326, default=
Point(15.3725629, 44.2396769))
    property_town = models.CharField(max_length=50,default="sana'a")# المدينة
    rent_frequency = models.CharField(max_length=50,default="monthly")
    ownership_type = models.CharField(max_length=20,null
=True,blank=True) #وقف أو حر 
    property_description = models.TextField(null=True,blank=True)
    property_price = models.IntegerField(null=True,blank
=True)
    phone = models.CharField(max_length=50,default="776278868")
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    rooms = models.CharField(max_length=50,default="2")
    baths= models.CharField(max_length=10,default="2")
    furnishingStatus = models.BooleanField(default=True)
    # geofence = gis_models.PolygonField(null=True,blank=True)
   # objects = PropertyManager() # for search
    def __str__(self):
        return self.req_order_title
    
    class Meta:
        verbose_name = _("Request_order")
        verbose_name_plural = _("Request_order")
    