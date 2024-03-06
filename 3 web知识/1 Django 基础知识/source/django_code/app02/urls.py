from django.contrib import admin
from django.urls import path, re_path, include

from app02.views import api_method1

urlpatterns = [
    path('api/01', api_method1)
]
