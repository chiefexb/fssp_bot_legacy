#!/usr/bin/python3
# -*- coding: utf-8 -*-
from lxml import etree
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
from telegram import ReplyKeyboardMarkup, KeyboardButton
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
level=logging.INFO)

logger = logging.getLogger(__name__)
reply_keyboard = [['Найти задолженность']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
CHOICE,SEARCH,NAME,LASTNAME=range(4)
facts={}
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Привет я робот судебный пристав!\n Чем могу быть полезен?",reply_markup=markup)
    return SEARCH
def search_ip(bot, update):
    text = update.message.text
    #logger.info("Gender of %s: %s", user.first_name, update.message.text)
    update.message.reply_text(
        "Введите имя")
    return NAME
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
    update.message.reply_text(
        str(facts['firstname'])+str(facts['lastname']))
    return LASTNAME
def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error) 
def main():
    logger.setLevel(logging.DEBUG)
    cfg = etree.parse('./config.xml') 
    cfgroot=cfg.getroot()
    telegram_param=cfgroot.find('telegram')  
    tg_token=telegram_param.find('token').text  
    
    updater = Updater(tg_token)
    dp = updater.dispatcher
    #start_handler = CommandHandler('start', start)
    #search_handler = CommandHandler('search', search_ip)
    #dp.add_handler(start_handler)
    #dp.add_handler(search_handler) 
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={   
            SEARCH: [RegexHandler('^(Найти задолженность)$', search_ip)],
            NAME: [MessageHandler(Filters.text,upd_name)],
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
