from django.shortcuts import render, HttpResponse


# Create your views here.

def app02_index(request):
    return HttpResponse("app02...")


def app02_index_year(request, year):
    print(type(year))
    return HttpResponse("app02..." + year)


def app02_index_month(request, year, month):
    return HttpResponse("2024/%s/%s" % (year, month))


def app02_index_month2(request, month, year):
    return HttpResponse("今年是%s/%s" % (year, month))


def api_method1(request):
    return HttpResponse("app02/api method1...")
