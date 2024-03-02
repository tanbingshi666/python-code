import datetime

from django.shortcuts import render, HttpResponse

from polls.models import Teacher, Subject


# Create your views here.

def index(request):
    return HttpResponse("hello index polls")


def create_teacher(request):
    # 联表插入
    # subject = Subject(name='语文', intro='国文', is_hot=True)
    # subject.save()
    # Teacher(name='tan',
    #         sex=True,
    #         birth=datetime.datetime.now(),
    #         intro='靓仔',
    #         photo='tan.jps',
    #         good_count=1,
    #         bad_count=1,
    #         subject=subject
    #         ).save()

    Subject.objects.create(name='数学', intro='逻辑', is_hot=False)

    return HttpResponse("创建老师成功")
