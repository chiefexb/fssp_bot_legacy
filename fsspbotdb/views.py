from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import  json
from fsspbotdb.models import *
import datetime
from django.shortcuts import get_object_or_404




def index (request):
    
    #t = get_template('templates/base.html')
    #now = datetime.datetime.now()
    #html = t.render(context=None, request=None)
    #p=Task.objects.filter(thash=gt['hash'])
    #p=Task.objects
    #a=p.values_list()
    #p2=Task.objects.all()
    html="HHH"
    #t = get_template('templates/base.html')
    now = datetime.datetime.now()
    #html = t.render(context={'tasks':p2}, request=None)
    return HttpResponse(html)
def webhook (request,slug):
    print(slug)
    p=Setting.objects.filter(valuename='TELETOKEN')
    html=slug
    
    #str(p.values()[0]['value'].split(',')[0])
             #p.values()[0]['value']
    #if slug=='/'+p.values()[0]['value']:
    #    html=OK
    #else:
     #  raise Http404("does not exist")
    return HttpResponse(html)
