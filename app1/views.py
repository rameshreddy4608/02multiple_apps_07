from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_app1(request):
    return HttpResponse('<h1>this is my fist app1 project</h1>')


def second_app1(request):
    return HttpResponse('<h1>this is second_app1 project</h1>')
