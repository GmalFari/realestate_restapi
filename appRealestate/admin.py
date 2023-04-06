from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Property,Country,City,State
# Register your models here.
@admin.register(Property)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('location',)

@admin.register(Country)
class CountryAdmin(OSMGeoAdmin):
    list_display = ('location',)


@admin.register(State)
class StateAdmin(OSMGeoAdmin):
    list_display = ('location',)


@admin.register(City)
class CityAdmin(OSMGeoAdmin):
    list_display = ('location',)





