from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, id, nickname):
    result = 'id: ' + str(id) + ', name: "' + nickname + '".'
    return HttpResponse(result)