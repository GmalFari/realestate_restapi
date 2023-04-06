from rest_framework import generics , viewsets, authentication ,permissions
from django.shortcuts import render,get_object_or_404
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.gis.geos import GEOSGeometry
from rest_framework_gis.pagination import GeoJsonPagination

import json
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
# headers = {
# 	"X-RapidAPI-Key": "6cb10cae22mshe83ac21e4eb1de3p1897c1jsn0b3893d5488f",
# 	"X-RapidAPI-Host": "bayut.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.json())

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
    # pagination_class = GeoJsonPagination

    authentication_classes = [
                            # authentication.SessionAuthentication,
                              authentication.TokenAuthentication
                            ]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def get_queryset(self):
    #     user = self.request.user
        
    #     if user.id == None:
    #         return Property.objects.none()
        # 
        # return Property.objects.all().filter(user=user)
    def perform_create(self, serializer):
        # point = GEOSGeometry('POINT(%s %s)'%("22332","3232"))
        # if self.request.location:
            # locationData = json.loads(self.request.location)
        if self.request.user == None:
            serializer = serializer.save(user=self.request.user.pk)
        return super().perform_create(serializer)
class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    
    serializer_class = PropertySerializer
    permission_classes = [IsOwnerOrReadOnly]
    ordering_fields = ['timestamp']
    search_fields = ['property_title']
    


class CountryListCreateView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StatetListCreateView(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    
class CityListCreateView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    
# 


@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message":"Secret message"})

@api_view()
@permission_classes([IsAuthenticated])
def normal_user(request):
    if request.user.groups.filter(name='normal_users').exists():
        return Response({"message":"this is normal user"})
    else:
        return Response({'message':'not allowed in this group'})
