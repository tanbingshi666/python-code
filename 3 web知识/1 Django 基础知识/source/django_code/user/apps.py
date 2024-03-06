from django.apps import AppConfig
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.views import View


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'


class MiddleWareUser(MiddlewareMixin):
    def process_request(self, request):
        print("用户应用中间件请求...")

    def process_response(self, request, response):
        print("用户应用中间件响应...")
        return response


class IndexView(View):
    def get(self, request):
        return HttpResponse("this is get page")

    def post(self, request):
        return HttpResponse("this is post page")
