from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers
from rest_framework_gis.serializers import GeoModelSerializer
from django.contrib.auth.models import User
# from rest_framework_gis.serializers import GeoFeatureModelSerializer
import bleach
from .models import Property,Person,Country,State,City
from drf_extra_fields.fields import Base64ImageField
from django.core.files import File
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class PropertySerializer(GeoModelSerializer):
    coverPhoto = Base64ImageField(required=False)
    # location = gis_serializers.GeometryField(help_text='GeoJSON polygon defining region')
    class Meta:
        model = Property
        geo_field = "location"
        id_field = "id"
        # auto_bbox = True

        fields = '__all__'
    
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
        # if validated_data['coverPhoto']:
        obj = validated_data.pop('coverPhoto')
        print(obj)
            # print(obj)
            # coverPhoto = validated_data.pop('coverPhoto')
            # print(coverPhoto)
        created_item = Property.objects.create(coverPhoto=None)
            # created_item.coverPhoto = coverPhoto
        created_item.save()
        return created_item
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