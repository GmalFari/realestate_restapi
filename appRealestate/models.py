from django.urls import reverse
from django.db.models import Q
from django.contrib.gis.db import models as gis_models
from django.db.models.signals import pre_save,post_save
from django.utils.text import slugify
from django.db import models
from accounts.models import UserAccount
from smart_selects.db_fields import ChainedForeignKey 
from django_countries.fields import CountryField
from django.contrib.gis.geos import Point
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from .utils import path_file_name , img_file_name, slugify_instance_company

# Create your models here.
"""
-global
    Property 

    pictures
-user

    Property 
    pictures

company 
alternatives

additional info if was dept or building or land 

"""
# class PropertyQuerySet(models.QuerySet):
#     def search(self,query=None):
#         if query is None or query=="":
#             return self.none()
#         lookups =( Q(property_title__icontains=query) 
#         )
#         return self.filter(lookups)

# class PropertyManager(models.Manager):
#     def get_queryset(self):
#         return PropertyQuerySet(self.model,using=self._db)
#     def search(self,query=None):
#         return self.get_queryset().search(query=query)

class Person(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)


def upload_to(instance,filename):
    return f'media/{filename}'

class Property(models.Model):
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
    property_slug = models.SlugField(null=True,blank=True) 
    property_title = models.CharField(max_length=250)
    coverPhoto = models.ImageField(upload_to=upload_to,null=True,blank=True)
    purpose = models.CharField(max_length=20,null=True,blank=True) # للبيع للإيجار
    location = gis_models.PointField(srid=4326, default=Point(15.3725629, 44.2396769))
    property_town = models.CharField(max_length=50,default="sana'a")# المدينة
    rent_frequency = models.CharField(max_length=50,default="monthly")
    ownership_type = models.CharField(max_length=20,null=True,blank=True) #وقف أو حر 
    property_description = models.TextField(null=True,blank=True)
    property_area = models.ForeignKey('Country',on_delete=models.SET_NULL,null=True,blank=True) # المنطقة
    property_price = models.IntegerField(null=True,blank=True)
    is_negotiable = models.BooleanField(default=False)# قابلية التفاوض
    phone = models.CharField(max_length=50,default="776278868")
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    rooms = models.CharField(max_length=50,default="2")
    baths= models.CharField(max_length=10,default="2")
    furnishingStatus = models.BooleanField(default=True)
    # geofence = gis_models.PolygonField(null=True,blank=True)


   # objects = PropertyManager() # for search

    def __str__(self):
        return self.property_title
    
    class Meta:
        verbose_name = _("Property")
        verbose_name_plural = _("Properties")
    



class LocationHierarchy(models.Model):
    level = models.SmallIntegerField()
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True,blank=True)
    externalID = models.IntegerField()
    location = gis_models.PointField(srid=4326,null=True,blank=True)



# class PhoneNumber(models.Model):
#     mobile = 


class Country(models.Model):
    name = CountryField()
    slug = models.SlugField(null=True,blank=True)
    externalID = models.IntegerField()
    location = gis_models.PointField(null=True,blank=True)
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = _("country")
        verbose_name_plural = _("countries")
    

class State(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    name = models.CharField(_('State'), max_length=255, null=True)
    slug = models.SlugField(null=True,blank=True)
    externalID = models.IntegerField()
    location = gis_models.PointField(null=True,blank=True)

    def __str__(self):
        return str(self.name)

class City(models.Model):
    country =  models.ForeignKey(Country,on_delete=models.CASCADE)
    state = ChainedForeignKey('State', chained_field="country", chained_model_field="country", show_all=False, auto_choose=True)
    name = models.CharField(_('City'), max_length=255, null=True)
    slug = models.SlugField(null=True,blank=True)
    externalID = models.IntegerField()
    location = gis_models.PointField(null=True,blank=True)
    l = models
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")
    