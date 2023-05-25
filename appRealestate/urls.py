from django.urls import path
# from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    PersonListView,
    PropertyListView,
    PropertyDetailView

)
urlpatterns = [
    path('list-persons/',PersonListView.as_view()),
    path('list-properties/',PropertyListView.as_view()),
    path('list-properties/<int:pk>/',PropertyDetailView.as_view(),name="property"),
    
  
    # path('api-token-auth/',obtain_auth_token),
    
]
