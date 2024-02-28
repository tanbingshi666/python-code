"""django_code URL Configuration

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
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, re_path, include, register_converter

from app01.views import index, get_timer, index_html, index_html2, app01_login, app01_info
from app02.views import app02_index, app02_index_year, app02_index_month, app02_index_month2


# 自定义路由转发器
class PhoneConverter(object):
    # 正则表达式
    regex = r'1[3-9]\d{9}'

    def to_python(self, value):
        return int(value)


# 注册
register_converter(PhoneConverter, 'phone')


def phone_number(request, p):
    print(type(p), p)
    return HttpResponse(str(p) + "用户")


urlpatterns = [
    path('admin/', admin.site.urls),

    # 一般路由
    path('index/', index),
    # 动态数据返回
    path('timer/', get_timer),
    # 一般路由 html
    path('html/', index_html),
    # 动态数据返回 html
    path('html2/', index_html2),
    # 映射路径可以多对一视图函数 但是路径相同只取第一个定义视图函数
    path('', index_html),

    # 正则和简单分组
    # path('app02/2024', app02_index),
    # $ 表示结束 比如 app02/2024 不加 $ 会匹配 app02/2024/8 导致覆盖其他 re_path
    re_path('app02/\d{4}$', app02_index),
    # 如果想要提取路径的值 需要分组 也即 ()
    re_path('app02/year/(\d{4})', app02_index_year),
    # 无名分组 参数依次传入视图函数
    re_path('app02/month/(\d{4})/(\d{1,2})', app02_index_month),
    # 有名分组 根据路径分组名传参到视图函数
    re_path('app02/(?P<year>\d{4})/(?P<month>\d{1,2})', app02_index_month2),

    # 路由分发到不同的应用
    path('app01/', include('app01.urls')),
    path('app02/', include('app02.urls')),

    # 路由转发到自定义转换器
    path('index/<phone:p>', phone_number),

    # 请求方式 (Post Get)
    path('login/', app01_login),
    path('info/', app01_info),

    # 请求方式和参数
    path('user/', include("user.urls"))
]
