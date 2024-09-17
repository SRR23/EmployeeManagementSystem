
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', Home, name='home'),
    path('add_employee/', add_employee, name='add_employee'),
]
