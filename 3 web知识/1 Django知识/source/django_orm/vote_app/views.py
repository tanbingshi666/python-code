import datetime
import json

from django.core import serializers
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_http_methods

from vote_app.models import Subject, Teacher


# Create your views here.

def index(request):
    return HttpResponse("this is vote app index page")


def create(request):
    # 联表插入
    subject = Subject(name='语文', intro='国文', is_hot=True)
    subject.save()
    Teacher(name='TanBingShi',
            sex=True,
            birth=datetime.datetime.now(),
            intro='你是个靓仔',
            photo='tan.jps',
            good_count=1,
            bad_count=1,
            subject=subject
            ).save()

    # 单条记录插入
    # Subject.objects.create(name='数学', intro='逻辑', is_hot=False)

    return HttpResponse("联表创建老师和课程记录...")


@require_http_methods(["POST"])
def create_subject(request):
    # 字节类型
    body = request.body

    # 字典类型
    body_json = json.loads(body, encoding='utf-8')

    subject_name = body_json['name']
    subject_intro = body_json['intro']
    subject_is_hot = body_json['is_hot']

    # 插入成功返回
    subject = Subject.objects.create(name=subject_name, intro=subject_intro, is_hot=subject_is_hot)
    result = {'id': subject.no, 'code': 200, 'msg': '新增课程记录成功'}

    return JsonResponse(result)


def delete_subject(request, no):
    if request.method == 'POST':
        return JsonResponse({'code': 200, 'msg': '删除课程不支持 POST 请求'})
    elif request.method == 'DELETE':
        Subject.objects.get(no=no).delete()
        return JsonResponse({'code': 200, 'msg': 'ok'})
    elif request.method == 'PUT':
        return JsonResponse({'code': 200, 'msg': '删除课程不支持 PUT 请求'})
    else:
        return JsonResponse({'code': 200, 'msg': '删除课程不支持 GET 请求'})


def update_subject(request):
    if request.method == 'POST':
        body = request.body
        body_json = json.loads(body, encoding='utf-8')

        subject = Subject.objects.get(no=body_json['no'])
        subject.name = body_json['name']
        subject.intro = body_json['intro']
        subject.is_hot = body_json['is_hot']
        subject.save()
        return JsonResponse({'code': 200, 'msg': 'ok'})
    else:
        return JsonResponse({'code': 200, 'msg': '更新课程不支持 %s 请求' % request.method})


def query_subject(request):
    subjects = Subject.objects.all()
    subjects_json_str = serializers.serialize('json', subjects)
    subjects_json = json.loads(subjects_json_str)
    return JsonResponse({'code': 200, 'msg': 'ok', 'data': subjects_json})


def query_subject_by_id(request, no):
    subject = Subject.objects.get(no=no)
    subject_dict = model_to_dict(subject)
    return JsonResponse({'code': 200, 'msg': 'ok', 'data': subject_dict})
