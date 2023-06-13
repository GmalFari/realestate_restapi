from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Property,Country,City,State,PropertyMedia
# Register your models here.

@admin.register(PropertyMedia)
class propertyMediaAdmin(OSMGeoAdmin):
    list_display = ('property','image')
@admin.register(Property)
class ShopAdmin(OSMGeoAdmin):
    list_display = ("property_title","location",)

@admin.register(Country)
class CountryAdmin(OSMGeoAdmin):
    list_display = ('location',)


@admin.register(State)
class StateAdmin(OSMGeoAdmin):
    list_display = ('location',)


@admin.register(City)
class CityAdmin(OSMGeoAdmin):
    list_display = ('location',)





