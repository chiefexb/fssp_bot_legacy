from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import  json
from fsspbotdb.models import *
import datetime
from django.shortcuts import get_object_or_404

import telegram
from django.views.decorators.csrf import csrf_exempt

global bot 

p=Setting.objects.filter(valuename="TELETOKEN")
bot = telegram.Bot(token=p.values()[0]['value'])
del p

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
def set_webhook (request):
#curl -F “url=https://<YOURDOMAIN.EXAMPLE>/<WEBHOOKLOCATION>"
# https://api.telegram.org/bot<YOURTOKEN>/setWebhook
   # 'https://fssp.robointerativo.ru/HOOK'
    s = bot.setWebhook('https://fssp.robointerativo.ru/HOOK')
    if s:
        html="webhook setup ok"
    else:
        html= "webhook setup failed"
    return HttpResponse(html)


@csrf_exempt
def webhook(request):
    html=''
    if request.method == "POST":
        #f=open('/home/bot.log','a')
        # retrieve the message in JSON and then transform it to Telegram object
        #f.write(str(request.body)+'\n')
        #update = telegram.Update.de_json(request.get_json(force=True), bot)
        j=json.loads(bytes.decode(request.body) )
        update = telegram.Update.de_json(j, bot)
        chat_id = update.message.chat.id
        update_id= update.update_id
        # Telegram understands UTF-8, so encode text for unicode compatibility
        text = update.message.text.encode('utf-8')
        #f.write(str(type(update))+str(text)+str(update_id)+'\n')
        #f.close()
        html='OK'
        # repeat the same message back (echo)
        bot.sendMessage(chat_id=chat_id, text=text)
        bot.sendMessage(chat_id=update.message.chat_id, text='Hello, there')
        #request.body
    return HttpResponse (html)
