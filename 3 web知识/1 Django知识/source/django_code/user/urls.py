from django.contrib import admin
from django.urls import path, re_path, include

from user.views import index, index2, index3

urlpatterns = [
    # 请求方式为 GET
    path('index/', index),
    # 请求方式为 POST
    path('index2/', index2),
    # 返回响应数据
    path('index3/', index3)
]
