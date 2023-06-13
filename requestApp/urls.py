from django.urls import path                                             
from .views import (
        ReqOrderView,
       ReqOrderDetailView
  )


urlpatterns = [

       path('',ReqOrderView.as_view()),
          path('<str:pk>/',ReqOrderDetailView.as_view())
   
          ] 