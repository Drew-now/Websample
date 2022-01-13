from django.urls import path
from django.urls.conf import  path 
from .views import main



urlpatterns = [
    path('', main)
]