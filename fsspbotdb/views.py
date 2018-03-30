from fsspbotdb.fsspapi import *
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import  json
from fsspbotdb.models import *
import datetime
from django.shortcuts import get_object_or_404

from telegram.ext import Dispatcher
import telegram
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
from telegram import ReplyKeyboardMarkup, KeyboardButton

from django.views.decorators.csrf import csrf_exempt
import logging

global bot 

p=Setting.objects.filter(valuename="TELETOKEN")
bot = telegram.Bot(token=p.values()[0]['value'])
del p

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = '/home/bot.log')

def start (bot,update):
    #update.message.reply_text('Thank you! I hope we can talk again some day.')
    bot.send_message(chat_id=update.message.chat_id, text="Привет я робот судебный пристав!\n Чем могу быть полезен?",reply_markup=markup)
    return SEARCH
 

reply_keyboard = [['Найти задолженность']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

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
def dispatcher (update):
    user_id         = update.message.from_user.id
    update_id       = update.update_id
    message_date    = update.message.date
    message_id      = update.message.message_id
    p1=Telegram_session.objects.filter(user_id=user_id, status = 10)
    id= token=p.values()[0]['id']
    p2=Telegram_session (id=id,user_id = user_id, update_id=update_id, message_date=message_date, message_id=message_id, status=0  )
    p2.save()
def set_webhook (request):
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
        #f.write(str(request.body)+'\n')
        logging.info( str( request.body) )
        j= json.loads(request.body.decode())
        try:
            update = telegram.Update.de_json(j, bot)
        except:
            #f.write('ERR init update'+'\n')
            logging.error('ERR init update')
        else:
            #f.write('init update'+'\n')
            logging.info('start init update')
            try:
                dispatcher (update )      
                #st.callback(bot,update)
                #dp.process_update(update)
            except:
                #f.write('ERR HANDLERS'+'\n')
                logging.error('ERR init update')
                #f.write(sys.exc_info()[0])
        html=request.body.decode()

        #f.close()

    return HttpResponse (html)
