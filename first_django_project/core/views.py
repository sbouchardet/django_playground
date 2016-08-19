# Create your views here.
from django.shortcuts import render

def home(request):
        context = {'texto': 'Seu primeiro projeto Django no Linux/Ubuntu com Sublime Text 3'}

        return render(request, 'index.html', context)

def test(request):
    return render(request,'test.html')
