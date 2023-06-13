from django.http import JsonResponse
from rest_framework import generics , viewsets, authentication ,permissions
from rest_framework.views import APIView
from django.shortcuts import render,get_object_or_404
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.gis.geos import GEOSGeometry
from rest_framework_gis.pagination import GeoJsonPagination
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser,JSONParser
from django_filters.rest_framework import DjangoFilterBackend 
import json
from django.core.files import File


from .models import( 
                    Property ,
                    PropertyMedia,
                    Person,
                    Country,
                    State,
                    City
                    )
from .serializers import(
                        PropertySerializer , 
                        MediaSerializer,
                        PersonSerializer ,
                        CountrySerializer,
                        StateSerializer,
                        CitySerializer
                        )
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .permissions import IsOwnerOrReadOnly
import random
# helper function for save multiple images 
from .helper import modify_input_for_multiple_files
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
    # filter_backends=[DjangoFilterBackend]
    parser_classes = (FormParser,MultiPartParser,JSONParser)

    # pagination_class = GeoJsonPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filterset_fields = ('property_title','purpose', 'property_price','purpose','property_town')
    search_fields = ['property_title', 'purpose','property_price']
    # search_filter_class = SearchFilter(case_insensitive=False, partial_match=False)
    # def get_queryset(self, *args, **kwargs):
    #     qs =Property.objects.all()
    #     print(self.args)
    #     # q = self.request.query_params.get('property_title')
    #     # q = self.request.GET.get('q')
    #     results = Property.objects.none()
    #     # results = qs.search(q)
    #     # qs = qs.filter(property__property_title=q
    #     # )
    #     return qs
    
    # def post(self, request, *args, **kwargs):
    #     property_id = request.data['id']
    #     form_data = {}
    #     form_data['property']= property_id
    #     success = True
    #     response = []
    #     for images in request.FILES.getlist('test_file'):
    #         form_data['images']=images
    #         print(form_data)
    #         serializer = MediaSerializer(data=form_data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             response.append(serializer.data)
    #         else:
    #             success = False
    #     if success:
    #         #return Response(response, status=status.HTTP_201_CREATED)
           
    #         return Response({
    #         'status' : 1, 
    #         'message' : 'Success',
    #         'Data' : response,
    #         })
            
    #       #returnResponse(response,status=status.HTTP_400_BAD_REQUEST)

    #     return Response({
    #         'status' : 0, 
    #         'message' : 'Error!',
    #     })    

class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    
    serializer_class = PropertySerializer
    permission_classes = [IsOwnerOrReadOnly]
    ordering_fields = ['timestamp']
    search_fields = ['property_title']
    parser_classes = (JSONParser, MultiPartParser,FormParser,)
    

# class ImageAPIView(generics.ListCreateAPIView):
#     queryset = PropertyMedia.objects.all()
#     serializer_class = MediaSerializer
#     def post(self, request, *args, **kwargs):
#         property_id = request.data['property']
#         form_data = {}
#         form_data['property']= property_id
#         success = True
#         response = []
#         for images in request.FILES.getlist('images'):
#             form_data['images']=images
#             print(form_data)
#             serializer = PropertyImageSerializers(data=form_data)
#             if serializer.is_valid():
#                 serializer.save()
#                 response.append(serializer.data)
#             else:
#                 success = False
#         if success:
#             #return Response(response, status=status.HTTP_201_CREATED)
  



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

