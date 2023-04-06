from django.urls import path
# from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    PropertyListView,
    PropertyDetailView,

    CountryListCreateView,
    StatetListCreateView,
    CityListCreateView,

    PersonListView,
    secret,
    normal_user,
)
urlpatterns = [
    path('list-persons/',PersonListView.as_view()),
    path('list-properties/',PropertyListView.as_view()),
    path('list-properties/<int:pk>/',PropertyDetailView.as_view(),name="property"),
    
    path('countries/',CountryListCreateView.as_view(),name="countries"),
    path('states/',StatetListCreateView.as_view(),name="states"),
    path('cities/',CityListCreateView.as_view(),name="cities"),

    # path('api-token-auth/',obtain_auth_token),
    path('secret/',secret),
    path('normal-user/',normal_user),

]
