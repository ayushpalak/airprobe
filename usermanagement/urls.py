from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url

urlpatterns = [
    path('get_name', csrf_exempt(views.get_name) , name='get_name'),
    path('getEmployeeData', csrf_exempt(views.getEmployeeData) , name='getEmployeeData'),
    path('updateEmployeeData', csrf_exempt(views.updateEmployeeData) , name='updateEmployeeData'),
    
    
    
    
]
