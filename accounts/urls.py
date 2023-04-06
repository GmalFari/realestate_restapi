from django.urls import path
from .views import (
    RegisterView,
    RetrieveuserView
)
urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('me/',RetrieveuserView.as_view()),
    # path('profile/',PersonListView.as_view(),name="profile")
        
]
