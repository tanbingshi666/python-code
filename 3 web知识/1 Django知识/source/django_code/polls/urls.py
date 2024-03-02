from django.contrib import admin
from django.urls import path, re_path, include

from polls.views import index, create_teacher

urlpatterns = [
    path('index/', index),
    path('create/', create_teacher)
]
