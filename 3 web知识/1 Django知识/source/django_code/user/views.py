import json

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.http import require_http_methods


# Create your views here.
def index(request):
    # 默认请求方式可以为 GET POST
    print("请求方式:" + request.method)

    # 获取请求参数
    # <QueryDict: {'name': ['tan'], 'passwd': ['123456']}>
    # 可以看出 request.GET 返回是一个字典 其中 value 是一个 list 集合
    print(request.GET)
    # 默认获取 list 集合的最后一个元素
    print(request.GET.get('name'))

    # 获取请求路径
    # eg: /user/index/
    print(request.path)
    # eg: /user/index/?name=tan&passwd=123456
    print(request.get_full_path())

    # 获取请求头
    # 返回请求头信息 是一个 dict 类型
    print(type(request.META))
    # 需要注意的是 django 会将请求头的信息封装为 HTTP_ 前缀的 key-value
    # 比如请求头为 Accept-Encoding: gzip, deflate, br 被封装为 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br'
    print(request.META)
    print(request.META.get('HTTP_ACCEPT_ENCODING'))

    return HttpResponse("index")


@require_http_methods(["POST"])
def index2(request):
    # 请求方式为 POST
    print(request.method)

    # 获取请求 body
    # 字典类型 但是这种方式获取数据必须为 urlencoded 类型 否则为空
    # eg: <class 'django.http.request.QueryDict'>
    print(type(request.POST))
    # eg: <QueryDict: {'name': ['tan'], 'age': ['123']}>
    print(request.POST)
    # 这种方式适合我们常用的 json 对象 body
    # eg: <class 'bytes'>
    print(type(request.body))
    # eg: b'{\r\n    "name": "tan",\r\n    "age": 123\r\n}'
    print(request.body)
    # 返回字典类型
    # json_data = json.loads(request.body.decode('utf-8'))
    # print(json_data)

    return HttpResponse("index2")


def index3(request):
    print("请求方式: " + request.method)

    # 响应 json 数据
    # book = {'name': '武林外传', 'price': 998}
    # return HttpResponse(json.dumps(book, ensure_ascii=False), content_type='application/json')
    # return JsonResponse(book)

    # 序列号 list json 数据
    # books = [{'name': '武林外传1', 'price': 999}, {'name': '武林外传2', 'price': 998}]
    # return JsonResponse(books, safe=False)

    # 自定义响应头
    # resp = HttpResponse("index3")
    # resp['custom-user'] = 'tan'
    # return resp

    # 渲染返回
    # return render(request, "index.html", {'ip': '192.168.127.12'})

    # 重定向返回
    # 客户端请求到这里 django 向客户端发送下一个请求路径 也即请求 /user/index
    # 因此重定向会发送两次请求
    return redirect('/user/index')


def middle_ware(request):
    return HttpResponse("hello middle ware")
