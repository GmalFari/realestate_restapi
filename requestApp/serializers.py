from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers
from rest_framework_gis.serializers import GeoModelSerializer
from django.contrib.auth.models import User
from .models import Req_order
class Req_order_serializer(serializers.ModelSerializer):
    class Meta:
        model = Req_order
        fields = "__all__"
