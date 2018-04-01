from fsspbotdb.fsspapi import *
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
def get_active_session (j):
    logging.info('get_act '+str(j))
    chat_id=j['message']['chat']['id']
    p=Telegram_session.objects.filter(chat_id=chat_id).exclude(status=10)
    cnt=p.count()
    if cnt>0:
       lst=p.order_by('message_date').values().last()
    else:
       lst=[]
    return lst
    #start_session
def session_stop(j):
    p=get_active_session(j)
    try:
        id=p['id']
    except:
        pass
    else:
        p2=Telegram_session.objects.filter(id=id)
        p2.update(status=10)
def session_start(j):
     upd_id   = j['update_id']
     usr_id   = j['message']['from']['id']
     msg_id   = j['message']['message_id']
     msg      = j['message']['text']
     msg_date = datetime.datetime.fromtimestamp(j['message']['date']) 
     chat_id=j['message']['chat']['id']
     p=Telegram_session (update_id=upd_id,message=msg, message_id=msg_id,user_id=usr_id,chat_id=chat_id,message_date=msg_date,status=0)
     try:
         p.save()
     except:
         logging('error add session')
def save_cookies(j,name,val):
     upd_id   = j['update_id']
     usr_id   = j['message']['from']['id']
     msg_id   = j['message']['message_id']
     msg      = j['message']['text']
     msg_date = datetime.datetime.fromtimestamp(j['message']['date'])
     chat_id=j['message']['chat']['id']
     p=Cookie.objects.filter(user_id=usr_id, valuename=name)
     if p.count()>0:
         p.update(value=val)
     else:
         p=Cookie(user_id=usr_id,valuename=name,value=val)
         p.save()
def send_contact (chat_id,phone,name):
    p=Setting.objects.filter(valuename="TELETOKEN")
    token =p.values()[0]['value']
    del p
    url='https://api.telegram.org/bot'+token+'/sendContact'
    answer={'chat_id':chat_id,'phone_number':phone,'first_name':name}
    r=requests.post (url,data=answer)
    return r.json()
def send_message(chat_id,text):
    p=Setting.objects.filter(valuename="TELETOKEN")
    token =p.values()[0]['value']
    del p
    url="https://api.telegram.org/bot"+token+'/sendMessage'
    answer={'chat_id':chat_id, 'parse_mode':'HTML','text':text}
    try:
        r=requests.post (url,data=answer)
    except:
        logging.err( 'ERR in send' )
    else:
        logging.info('SEND '+ r.text )
        return r.json()
    return '1' 
def ipsearch (j):  
    #start_session
    logging.info('in search ip ' )
    upd_id   = j['update_id']
    chat_id=j['message']['chat']['id']
    usr_id   = j['message']['from']['id']
    p=get_active_session(j)
    #logging.info('in search p='+type(p) )
    if  len (p)>0:
        stp=upd_id-p['update_id']
        #if stp==1:
        #    send_message(chat_id,'Step='+str(stp) )
        #    send_message(chat_id,'Ваш регион ?' +  j['message']['text'])
        if stp==1:
            send_message(chat_id,'Step='+str(stp) )
            send_message(chat_id,'Введите имя для поиска?' +  j['message']['text'])
            save_cookies(j,'search_region', j['message']['text'] )
        if stp==2:
            send_message(chat_id,'Step='+str(stp) )
            send_message(chat_id,'Введите фамилию для поиска? ' +  j['message']['text'])
            save_cookies(j,'search_firstname', j['message']['text'] )
        if stp==3  :
        #    sen_message(chat_id,'Step='+str(stp) )
            save_cookies(j,'search_lastname', j['message']['text'] )
            send_message(chat_id,'Все готово ищем...' )
            #-------------
            p=Setting.objects.filter(valuename="FSSPTOKEN")
            token =p.values()[0]['value']
            del p
            api2=FsspApi(token)
            #print('TOKEN='+facts['token'])
            p=Cookie.objects.filter(valuename="search_region", user_id= usr_id )
            region =p.values()[0]['value']
            p=Cookie.objects.filter(valuename="search_lastname",user_id=usr_id)
            lastname =p.values()[0]['value']
            p=Cookie.objects.filter(valuename="search_firstname",user_id=usr_id)
            firstname =p.values()[0]['value']

            api2.set_region(region)
            api2.set_firstname(firstname)
            api2.set_lastname(lastname)
            api2.search_phisycal()
            save_cookies(j,'search_task', api2.task )
        if stp>3  :
            p=Setting.objects.filter(valuename="FSSPTOKEN")
            token =p.values()[0]['value']
            p=Cookie.objects.filter(valuename="search_task",user_id=usr_id)
            task =p.values()[0]['value']
            api2=FsspApi(token)
            api2.task=task          
            #print (api.get_status_task())
            #api2.wait_for(
            st=api2.get_status_task()
            logging.info('SEARCH '+str( st ) )
            send_message(chat_id,'SEARCH '+str( st ) )
            if (st):
                session_stop(j)
                api2.get_result()
                #formtext=
                #print (api2.result)
                if len(api2.result)>0:
                    for  rez in api2.result:
                        send_message(chat_id,text='=======================' )
                        for m in format_ip(rez):
                           #logger.info(user.first_name,user.last_name,user.id,m)
                             try:
                                send_message(chat_id,text=m )
                             except:
                                send_message(chat_id,text=m )
                else: send_message(chat_id ,text='<b>НЕ НАЙДЕНО ИСПОЛНИТЕЛЬНЫХ ПРОИЗВОДСТВ</b> ')
            else:
                send_message(chat_id ,text='Нет ответа, нажмите /retry')
            #send_message(j, text="Привет я робот судебный пристав!\n Чем могу быть полезен? /start")
    
            #------------
    else:
        session_start(j)
        #Спросить регион
        send_message(chat_id,'Назовите код региона, для поиска?')
    #Спросить Имя
    #Спросить Фамилию 
def parser(j):
    try:
        chat_id = j['message']['chat']['id']
    except:
        logging.error('Error in parser '+str(j) )
    else:
        user_id = j['message']['from']['id']
        text    = j['message']['text']
        upd_id   = j['update_id']
        #send_message(chat_id,'TEST')
        #send_message(chat_id,text)
        #text=
        p=get_active_session(j)
        #logging.info('in search p='+type(p) )
        if  len (p)>0:
            if p['message']=='/search':
                ipsearch(j)
        if ('text' in j['message'].keys() and len (p)<=0):  
            if text == '/start':
                send_message(chat_id,'Здравствуйте я бот-судебный пристав исполнитель: \n'+
             'для поиска по базе должников наберите /search \n'+
             'чтобы узнать обо мне наберите /about'  )
            if text=='/cookies':
                pass
            if text == '/search':
            #session_start (j)
               u=j
               try:
                   a=ipsearch ( u )
               except:
                   e = sys.exc_info()[0]
                   logging.error('Error while search '+ str(e) )
                   #logging.error('Error in search '+ str( type(j)  )
                   #r=send_message(chat_id,'В данный момент я на техобслуживании, \n'+
                   #'воспользуйтесь пока официальным сайтом https://fssprus.ru/iss/ip/ или попробуйте позже.')
                   #'Введите Фамилию Имя через пробел')
                   #logging.info(r)
            if text == '/about':
                r=send_message(chat_id,'Бот создан Алексеем Шило @Alexpricker \n   '+
            'сайт проекта https://robointerativo.ru')
            #r2=send_contact(chat_id,'@Alexpricker','+79631713818','Алексей')
            #'Введите Фамилию Имя через пробел')
            #logging.info(str(r))
            #logging.info( str(r2))

@csrf_exempt
def webhook(request):
    html=''
    if request.method == "POST":
        #f=open('/home/bot.log','a')
        #f.write(str(request.body)+'\n')
        logging.info('WEBHOOK '+ str( request.body) )
        j= json.loads(request.body.decode())
        parser(j)
        #chat_id=j['message']['chat']['id']
        #err=send_message(chat_id,str(j))
        #logging.info( str( err) )
        html=request.body.decode()

        #f.close()

    return HttpResponse (html)
