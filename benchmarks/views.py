# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
def index(request):
    # return HttpResponse("Hello World")
    return render_to_response('benchmarks/index.html',{"page":"benchmarks"}, context_instance=RequestContext(request))# Create your views here.
