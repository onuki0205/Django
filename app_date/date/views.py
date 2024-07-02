from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm

class HelloView(TempleteView):
    def __init__(self):
        self.params = {
            'title': 'Hello',
            'form': HelloForm(),
            'result': None
        }

    def get(self, request):
        return render(request, 'date/index.html', self.params)
    
    def post(self, request):
        if('check' in request.POST):
            self.params['result'] = 'checked!'
        else:
            self.params['result'] = 'not checked'
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'date/index.html', self.params)