"""django_orm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path

from vote_app.views import index, create, create_subject, delete_subject, update_subject, query_subject, \
    query_subject_by_id

urlpatterns = [
    path('', index),
    path('create/', create),
    path('api/create/subject', create_subject),
    re_path(r'api/delete/(?P<no>\d)/subject', delete_subject),
    path('api/update/subject', update_subject),
    path('api/query/subject', query_subject),
    re_path(r'api/query/(?P<no>\d)/subject', query_subject_by_id),
]
