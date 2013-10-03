from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect

def index(request):
    # return HttpResponse("Hello World")
    # redirect('home.views.index')
    return render_to_response('home/index.html',{"page":"home", "loop":[i for i in range(5)]}, context_instance=RequestContext(request))