from django.shortcuts import render
from django.http import HttpResponse

def base(request):
    return HttpResponse("<h1>Початкова сторінка<h1>")

def hello_world(request):
    return HttpResponse("<h1>Hello world 6<h1>", status=200)