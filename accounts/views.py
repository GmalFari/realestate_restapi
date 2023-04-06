# from rest_framework import generics , viewsets, authentication ,permissions
from rest_framework import (
            permissions,
            status)
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
# from .serializers import UserSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserCreateSerializer,UserSerializer

class RegisterView(APIView):
    def post(self,request):
        data = request.data
        print(data)
        serializer  = UserCreateSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        user = serializer.create(serializer.validated_data)
        user = UserSerializer(user)
        return Response(user.data,status=status.HTTP_201_CREATED)

class RetrieveuserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        user = request.user
        user = UserSerializer(user)
        return Response(user.data,status=status.HTTP_200_OK)
# class EmailTokenObtainPairView(TokenObtainPairView):
#     seriali
# zer_class = CustomTokenObtainPairSerializer

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Add custom claims
#         token['username'] = user.username
#         # ...

#         return token

# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer
