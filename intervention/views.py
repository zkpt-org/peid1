# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
def index(request):
    # return HttpResponse("Hello World")
    return render_to_response('intervention/index.html',{"page":"intervention"}, context_instance=RequestContext(request))