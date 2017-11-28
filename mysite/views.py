from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world！ This is my first trial. [Poll的笔记]")