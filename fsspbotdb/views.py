# from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# from django.template.loader import get_template
# from django.template import Context
import  json
from fsspbotdb.models import *
from api.fsspapi import *
import datetime
# from django.shortcuts import get_object_or_404
# import requests

from django.views.decorators.csrf import csrf_exempt
import logging
# import sys


logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.DEBUG, filename='/home/bot.log')


def index (request):
    
    html="HHH"
    now = datetime.datetime.now()
    return HttpResponse(html)


@csrf_exempt
def webhook(request):
    html='OK'
    c = {}
    logging.info('ALL MESS: '+ str( request.body) )
    if request.method == "POST":
        mes = request.body.decode('UTF8')
        j = json.loads(mes)
        p = Setting.objects.filter(valuename='FSSPTOKEN')
        fssptok=p.values()[0]['value']
        fssp=FsspApi(fssptok)
        fssp.lastname=j['queryResult']['parameters']['lastname']
        fssp.name=j['queryResult']['parameters']['name']
        fssp.region='09'
        fssp.search_phisycal()
        fssp.wait_for()

        logging.info('QResult' + str(j['queryResult']['parameters']))
        mess=fssp.result
        mm=''
        for m in mess:
            mm=mm+fssp.format_ip(m)
        c['fulfillmentText']=mm
        html = JsonResponse(c)

    return HttpResponse (html)
