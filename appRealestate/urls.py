from django.urls import path
# from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    PersonListView,
    PropertyListView,
    PropertyDetailView,
    # ImageView,

)
urlpatterns = [
    path('list-persons/',PersonListView.as_view()),
    path('list-properties/',PropertyListView.as_view()),
    path('list-properties/<str:pk>/',PropertyDetailView.as_view(),name="property"),

    # path('list-properties/<str:pk>/images/',ImageView.as_view())
    
  
    # path('api-token-auth/',obtain_auth_token),
    
]
