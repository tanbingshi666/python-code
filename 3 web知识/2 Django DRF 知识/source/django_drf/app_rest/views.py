from rest_framework.response import Response
from rest_framework.versioning import QueryParameterVersioning
from rest_framework.views import APIView


# Create your views here.
class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        '''
            request rest_framework 的 Request 对象 其封装了 Django 的 HttpRequest
            rest_framework 的 Request 对象的 _request 属性本质为 Django 的 HttpRequest
            因此 request._request 返回对象为 Django 的 HttpRequest

            request.query_params 底层调用 Django 的 HttpRequest.GET 返回 GET 请求参数 (类型为 QueryDict)
            eg: http://localhost:8000/rest/index?name=tan -> QueryDict{'name':'tan'}
        '''
        print(request._request.method)
        print(request.query_params.get("name"))

        return Response({"code": 1000, "data": "xxx"})

    def post(self, request, *args, **kwargs):
        '''
        request.data 获取请求体内容(字典类型) 比如 {"name":"tanbs"}
        eg: http://localhost:8000/rest/index/ body={"name":"tanbs"}
        '''
        print(request.data)
        return Response({"code": 1000, "data": "yyy"})


class VersionView(APIView):
    # GET 请求参数设置 eg: http://localhost:8000/rest/version/?version=v1
    # versioning_class = QueryParameterVersioning

    def get(self, request, *args, **kwargs):
        print(request.version)
        return Response({"code": 1000, "data": "version"})
