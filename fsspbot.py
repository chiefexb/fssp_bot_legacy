#!/usr/bin/python3
# -*- coding: utf-8 -*-
from lxml import etree
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
from telegram import ReplyKeyboardMarkup
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
level=logging.INFO)

logger = logging.getLogger(__name__)
reply_keyboard = [['Узнать задолженность']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Привет я робот судебный пристав!\n Чем могу быть полезен?",reply_markup=markup)
def search_ip(bot, update):
    update.message.reply_text(
        "Hi! My name is Doctor Botter. I will hold a more complex conversation with you. "
        "Why don't you tell me something about yourself?",
reply_markup=markup)

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
    start_handler = CommandHandler('start', start)
    searchip_handler = CommandHandler('search', search_ip)
    dp.add_handler(start_handler) 
    dp.add_handler(searchip_handler)
    updater.start_polling()
    updater.idle()
if __name__ == "__main__":
    main()
