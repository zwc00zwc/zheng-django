from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello world！ This is my first trial. [Poll的笔记]")

def index(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)