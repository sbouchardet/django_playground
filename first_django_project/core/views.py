# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
        # context = {'texto': 'Seu primeiro projeto Django no Linux/Ubuntu com Sublime Text 3'}
    ua = request.META['HTTP_USER_AGENT']  # Might raise KeyError!
    return HttpResponse("Your browser is %s" % ua)
    # return HttpResponse("Welcome to the page at %s" % request.path)

def test(request,question_id):
    return HttpResponse("<form action='/test/sbmt/'>You're voting on question %s.<input type='text' name='val'> <input type='submit' value='ok'/></form>" % question_id)

def test_post(request):
    return HttpResponse("veio %s" % str(request.POST.get('val')) );
