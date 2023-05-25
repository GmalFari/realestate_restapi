from rest_framework import generics , viewsets, authentication ,permissions
from django.shortcuts import render,get_object_or_404
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.gis.geos import GEOSGeometry
from rest_framework_gis.pagination import GeoJsonPagination
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser,JSONParser
from django_filters.rest_framework import DjangoFilterBackend 
import json
from django.core.files import File
from .models import( 
                    Property ,
                    Person,
                    Country,
                    State,
                    City
                    )
from .serializers import(
                        PropertySerializer , 
                        PersonSerializer ,
                        CountrySerializer,
                        StateSerializer,
                        CitySerializer
                        )
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .permissions import IsOwnerOrReadOnly
# Create your views here.

# import requests

# url = "https://bayut.p.rapidapi.com/auto-complete"

# querystring = {"query":"abu dhabi","hitsPerPage":"25","page":"0","lang":"en"}

class PersonListView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]
# 


class PropertyListView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    # throttle_classes = [AnonRateThrottle,UserRateThrottle]
    serializer_class = PropertySerializer 
    filter_backends=[DjangoFilterBackend]
    parser_classes = (JSONParser, MultiPartParser,FormParser,)

    # pagination_class = GeoJsonPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filterset_fields = ('property_title','purpose', 'property_price','purpose','property_town')
    search_fields = ['property_title', 'purpose','property_price']
    # search_filter_class = SearchFilter(case_insensitive=False, partial_match=False)
    def get_queryset(self, *args, **kwargs):
        qs =Property.objects.all()
        print(self.args)
        # q = self.request.query_params.get('property_title')
        # q = self.request.GET.get('q')
        results = Property.objects.none()
        # results = qs.search(q)
        # qs = qs.filter(property__property_title=q
        # )
        return qs
    
    def perform_create(self, serializer):
        print(serializer)
        # content = serializer.validated_data.get('property_title') or None
        # print(content)
        # point = GEOSGeometry('POINT(%s %s)'%("22332","3232"))
        # if self.request.location:
            # locationData = json.loads(self.request.location)
        if self.request.user == None:
            serializer = serializer(files=self.request.FILES)
            print(serializer.data)
        if self.request.status == 200:
            print("hello")
        return super().perform_create(serializer)



class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    
    serializer_class = PropertySerializer
    # permission_classes = [IsOwnerOrReadOnly]
    ordering_fields = ['timestamp']
    search_fields = ['property_title']
    parser_classes = (JSONParser,)
    def post(self, serializer):
        print(self.request.FILES)
        # content = serializer.validated_data.get('property_title') or None
        # print(content)
        # point = GEOSGeometry('POINT(%s %s)'%("22332","3232"))
        # if self.request.location:
            # locationData = json.loads(self.request.location)
        if self.request.user != None:
            serializer = PropertySerializer(files=self.request.FILES)
            print(serializer.data)
        print(serializer.data)

        return serializer.data



# class CountryListCreateView(generics.ListCreateAPIView):
#     queryset = Country.objects.all()
#     serializer_class = CountrySerializer
# class StatetListCreateView(generics.ListCreateAPIView):
#     queryset = State.objects.all()
#     serializer_class = StateSerializer
# class CityListCreateView(generics.ListCreateAPIView):
#     queryset = City.objects.all()
#     serializer_class = CitySerializer
    
# 

