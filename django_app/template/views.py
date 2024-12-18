from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    params = {
        'title' : 'Template/Index',
        'msg' : 'This is sample page.',
        'goto' : 'next',
    }
    return render(request, 'template/index.html', params)

def next(request):
    params = {
        'title' : 'Template/Next',
        'msg' : 'This is another page.',
        'goto' : 'index',
    }
    return render(request, 'template/index.html', params)