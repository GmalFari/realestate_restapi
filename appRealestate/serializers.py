from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers
from rest_framework_gis.serializers import GeoModelSerializer
from django.contrib.auth.models import User
from django.core.files import File
# from rest_framework_gis.serializers import GeoFeatureModelSerializer
import bleach
import random
from .models import (Property,PropertyMedia
        ,Person,Country,State,City)
from drf_extra_fields.fields import Base64ImageField
from django.core.files import File
from PIL import Image
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username']

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyMedia
        fields ="__all__"


class PropertySerializer(GeoModelSerializer):
    id = serializers.UUIDField(read_only=True)
    coverPhoto = serializers.ImageField(required=False)
    image = MediaSerializer(many=True,read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=True, use_url=False),
        write_only=True,required=False
    )
    # location = gis_serializers.GeometryField(help_text='GeoJSON polygon defining region')
    class Meta:
        model = Property
        geo_field = "location"
        id_field = "id"
        # auto_bbox = True

        fields = ["id","owner","property_title","property_slug" ,"coverPhoto",
                  "purpose","location","property_town","property_area",
                  "rent_frequency","ownership_type","property_description","property_price",
                  "currency","is_negotiable","phone","rooms","baths","furnishingStatus",
                  "building_facade","building_age","sqrt_area","omities","timestamp",
                  "updated","image","uploaded_images"
        ]

    
     
    
     
    
# geofence = gis]
    
    # def get_properties(self, instance, fields):
    #         # This is a PostgreSQL HStore field, which django maps to a dict
    #     return instance.location

    # def unformat_geojson(self, feature):
    #     attrs = {
    #         self.Meta.geo_field: feature["geometry"],
    #         "location": feature["properties"]
    #     }

    #     # if self.Meta.bbox_geo_field and "bbox" in feature:
    #     #     attrs[self.Meta.bbox_geo_field] = Polygon.from_bbox(feature["bbox"])


    #     return attrs
    def create(self,validated_data):

        uploaded_images = validated_data.pop("uploaded_images",None)
        cover_photo = validated_data.pop("coverPhoto",None)
        # sizes_img =Image.open(cover_photo)
        # size = 1280,720
        # sizes_img.thumbnail(size)
        # sizes_img.save()
        print(uploaded_images)
        obj = Property(**validated_data)
        if cover_photo != None:
            obj.coverPhoto.save(str(f"{random.randint(2222,24335534)}.png"),cover_photo)
        obj.save()
        if uploaded_images != None:
            for image in uploaded_images:
                PropertyMedia.objects.create(property=obj, image=image)
        # created_item = Property.objects.create

        #     # created_item.coverPhoto = coverPhoto
        # created_item.save()
        return obj
    def update(self, instance, validated_data):
        cover_photo = validated_data.pop("coverPhoto",None)
        sizes_img =Image.open(cover_photo)
        size = 1280,720
        sizes_img.thumbnail(size)
        sizes_img.save()

        print(sizes_img)
        if cover_photo != None:
            instance.coverPhoto.save(str(f"{random.randint(2222,24335534)}.png"),sizes_img)
            instance.save()
        instance = super().update(instance, validated_data)
        return instance
       


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'