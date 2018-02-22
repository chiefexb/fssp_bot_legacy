#!/usr/bin/python3
# -*- coding: utf-8 -*-
from lxml import etree,html
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
from telegram import ReplyKeyboardMarkup, KeyboardButton
import logging
from fsspapi import *
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
level=logging.INFO)

logger = logging.getLogger(__name__)
reply_keyboard = [['Найти задолженность']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
START,SEARCH,REG,FIRSTNAME,LASTNAME=range(5)

facts={}


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Привет я робот судебный пристав!\n Чем могу быть полезен?",reply_markup=markup)
    return SEARCH

  
def search_ip(bot, update):
    text = update.message.text
    #logger.info("Gender of %s: %s", user.first_name, update.message.text)
    update.message.reply_text(
        "Наберите код региона?")
  
    return REG
def upd_region(bot, update):
    text = update.message.text
    facts['region']=text
    #logger.info("Gender of %s: %s", user.first_name, update.message.text)
    update.message.reply_text(
        "Введите имя")
    return FIRSTNAME

def upd_name(bot, update):
    text = update.message.text
    facts['firstname']=text
    #logger.info("Gender of %s: %s", user.first_name, update.message.text)
    update.message.reply_text(
        "Введите фамилию")
    return LASTNAME
def upd_lastname(bot, update):
    text = update.message.text
    facts['lastname']=text
    #logger.info()
    #update.message.reply_text(
    #    str(facts['firstname'])+str(facts['lastname']))
    print (str(facts))
    api2=FsspApi(facts['token'])
    print('TOKEN='+facts['token'])
    api2.set_region(facts['region'])
    api2.set_firstname(facts['firstname'])
    api2.set_lastname(facts['lastname'])
    api2.search_phisycal()
    #print (api.get_status_task())
    api2.wait_for()
    api2.get_result()
    #formtext=
    print (api2.result)
    if len(api2.result)>0:
        for  rez in api2.result:
            bot.send_message(chat_id=update.message.chat_id,text='=======================' )
            for m in format_ip(rez):
                try:
                   bot.send_message(chat_id=update.message.chat_id,parse_mode='HTML',text=m )
                except:
                   bot.send_message(chat_id=update.message.chat_id,text=m )
    else:
        bot.send_message(chat_id=update.message.chat_id,parse_mode='HTML',text='<b>НЕ НАЙДЕНО ИСПОЛНИТЕЛЬНЫХ ПРОИЗВОДСТВ</b> ')
        
    bot.send_message(chat_id=update.message.chat_id, text="Привет я робот судебный пристав!\n Чем могу быть полезен?",reply_markup=markup)
    return SEARCH 
def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error) 
def format_ip(msg):
    fmsg=[]
    fmsg.append('<b>Должник (физ. лицо: ФИО, дата и место рождения; </b>')
    fmsg.append (msg['name'])
    fmsg.append ('<b>ИСПОЛНИТЕЛЬНОЕ ПРОИЗВОДСТВО:</b>')
    fmsg.append(msg['exe_production'])
    fmsg.append ('<b>ИСПОЛНИТЕЛЬНЫЙ ДОКУМЕНТ:</b>')
    fmsg.append(msg['details'])
    if len (msg['ip_end'])>0:
        fmsg.append ('<b>Дата окончания, статья</b>')
        fmsg.append(msg['ip_end']) 
    if len (msg['subject'])>0:
        fmsg.append ('<b>Предмет исполнения:</b>')
        fmsg.append(msg['subject'])
        
    fmsg.append ('<b>Отдел судебных приставов </b>')
    fmsg.append(msg['department'])
    fmsg.append ('<b>Судебный пристав исполнитель</b>')
    fmsg.append(msg['bailiff'].replace('<br>',' '))
   
    return fmsg
def main():
     
    logger.setLevel(logging.DEBUG)
    cfg = etree.parse('./config.xml') 
    cfgroot=cfg.getroot()
    telegram_param=cfgroot.find('telegram')  
    tg_token=telegram_param.find('token').text  
    fssp_param=cfgroot.find('fssp')  
    facts['token']=fssp_param.find('token').text  
    print (facts)
   
   


    
    updater = Updater(tg_token)
    dp = updater.dispatcher
   
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={   
            
            SEARCH: [RegexHandler('^(Найти задолженность)$', search_ip)],
            REG: [MessageHandler(Filters.text,upd_region)],
            FIRSTNAME: [MessageHandler(Filters.text,upd_name)],
            LASTNAME: [MessageHandler(Filters.text, upd_lastname)], 
        },

        fallbacks=[CommandHandler('cancel', cancel)]
     )
    dp.add_handler(conv_handler)
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()
if __name__ == "__main__":
    main()
