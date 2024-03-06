import datetime

from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_http_methods


# Create your views here.

def index(request):
    return HttpResponse("hello,index")


def get_timer(request):
    now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse(now_str)


def index_html(request):
    return render(request, 'index.html')


def index_html2(request):
    now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render(request, 'index2.html', {'now': now_str})


def api_method1(request):
    return HttpResponse("app01/api method1...")


@require_http_methods(["POST"])
def app01_login(request):
    return HttpResponse("app01 登录成功")


@require_http_methods(["GET"])
def app01_info(request):
    return HttpResponse("app01 信息")
