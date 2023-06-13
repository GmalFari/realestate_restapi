# Create your views from rest_framework import generics , viewsets, auth
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics , viewsets
# Create your views here.
from .models import (
        Req_order
        )

from .serializers import Req_order_serializer
class ReqOrderView(generics.ListCreateAPIView):
    queryset = Req_order.objects.all()
    serializer_class = Req_order_serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['req_order_title']

class ReqOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Req_order.objects.all()
    serializer_class = Req_order_serializer