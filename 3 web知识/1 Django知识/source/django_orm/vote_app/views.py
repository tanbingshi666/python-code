import datetime

from django.shortcuts import render, HttpResponse

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
