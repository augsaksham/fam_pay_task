from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    x=2
    y=1
    return HttpResponse('Hello World')