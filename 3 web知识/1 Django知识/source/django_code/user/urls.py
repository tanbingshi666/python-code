from django.contrib import admin
from django.urls import path, re_path, include

import user.apps
from user.views import index, index2, index3, middle_ware

urlpatterns = [
    # 请求方式为 GET
    path('index/', index),
    # 请求方式为 POST
    path('index2/', index2),
    # 返回响应数据
    path('index3/', index3),
    path('middle/', middle_ware),
    path('cbv/', user.apps.IndexView.as_view())
]
