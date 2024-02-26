from django.shortcuts import render, HttpResponse


# Create your views here.
def get_index(request):
    return HttpResponse("index")
