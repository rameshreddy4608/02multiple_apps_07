from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_app2(request):
    return HttpResponse('<h1>this is my first app2 projet</h1>')


def second_app2(request):
    return HttpResponse('<h1>this is my second_app2 projet</h1>')
    