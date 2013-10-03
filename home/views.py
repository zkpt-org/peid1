from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *
import json

def index(request):
    return render_to_response('home/index.html',{"page":"home", "loop":[i for i in range(5)]}, context_instance=RequestContext(request))

    
def dials(request):
    query = {}
    relevant = ('client', 'gender', 'age', 'condition', 'tenure')

    for param in relevant:
        if param not in request.GET.iteritems():
            query[param] = "ALL"
    
    query = dict(query.items() + dict([(param, val) for param, val in request.GET.iteritems()]).items())
    
    data = Metrics.objects.filter(**query).order_by('week').reverse()[0].json()

    return HttpResponse(json.dumps(data), content_type='application/json')

    
def graph(request):
    query = {}
    relevant = ('client', 'gender', 'age', 'condition', 'tenure')

    for param in relevant:
        if param not in request.GET.iteritems():
            query[param] = "ALL"
    
    query = dict(query.items() + dict([(param, val) for param, val in request.GET.iteritems()]).items())
            
    data = [metric.json() for metric in Metrics.objects.filter(**query).order_by('week')]

    return HttpResponse(json.dumps(data), content_type='application/json')

