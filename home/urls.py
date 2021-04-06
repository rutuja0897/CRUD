from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home),
    path('show',views.show),
    path('send',views.send)

]