from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import  json
from fsspbotdb.models import *
import datetime
from django.shortcuts import get_object_or_404
import requests

from django.views.decorators.csrf import csrf_exempt
import logging
import sys


logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = '/home/bot.log')

def index (request):
    
    html="HHH"
    now = datetime.datetime.now()
    return HttpResponse(html)

@csrf_exempt
def webhook(request):
    html=''
    #logging.info('WEBHOOK '+ str( request.body) )
    if request.method == "POST":
        logging.info('WEBHOOK '+ str( request.body) )
        logging.info('WEBHOOK '+ str( request.META) )
        #j= json.loads(request.body.decode())
        html=request.body.decode()


    return HttpResponse (status=200)
